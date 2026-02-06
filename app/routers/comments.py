from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.comment import Comment
from app.models.post import Post
from app.schemas.comment import CommentCreate

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/", status_code=201)
def create_comment(
    data: CommentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    post = db.query(Post).filter(
        Post.id == data.post_id,
        Post.is_deleted == False
    ).first()

    if not post:
        raise HTTPException(404, "Post not found")

    comment = Comment(
        content=data.content,
        post_id=data.post_id,
        user_id=user.id
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment
