from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.post import Post, PostStatus
from app.schemas.post import PostCreate, PostUpdate
from app.dependencies.permissions import require_admin , is_owner_or_admin

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", status_code=201)
def create_post(
    data: PostCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    post = Post(
        title=data.title,
        content=data.content,
        status=data.status,
        author_id=user.id
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).filter(
        Post.status == PostStatus.PUBLISHED,
        Post.is_deleted == False
    ).all()

@router.get("/{post_id}")
def get_post(
    post_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post or post.is_deleted:
        raise HTTPException(404, "Post not found")

    if post.status == PostStatus.DRAFT and post.author_id != user.id:
        raise HTTPException(403, "Not allowed to view draft")

    return post

@router.put("/{post_id}")
def update_post(
    post_id: int,
    data: PostUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(404)

    if not (user.role.value == "admin" or post.author_id == user.id):
        raise HTTPException(403, "Not allowed")

    post.title = data.title
    post.content = data.content
    post.status = data.status

    db.commit()
    return post

@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(404)

    if not (user.role.value == "admin" or post.author_id == user.id):
        raise HTTPException(403)

    post.is_deleted = True  
    db.commit()

    return {"message": "Post deleted"}

#check only admin can access this function
@router.get("/admin/all_post")
def get_all_users(
    db: Session = Depends(get_db),
    admin_user = Depends(require_admin)
):
    return db.query(Post).all()


@router.put("/posts/{post_id}")
def update_post(
    post_id: int,
    data: PostUpdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(404, "Post not found")

    if not is_owner_or_admin(post.author_id, user):
        raise HTTPException(403, "Not allowed to update this post")

    post.title = data.title
    post.content = data.content
    post.status = data.status

    db.commit()
    return post

@router.delete("/posts/{post_id}")
def delete_post(post_id:int,db:Session = Depends(get_db),user=Depends(get_current_user)):
    current_post = db.query(Post).filter(Post.id==post_id).first()
    print(current_post,'------current_post--------')

    if not current_post:
        raise HTTPException(404)

    if is_owner_or_admin(current_post.author_id,user):
        raise HTTPException(403,"Not allowed")
    
    current_post.is_deleted = True
    db.commit()

    return {"msg":"message deleted."}



