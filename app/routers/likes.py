from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.like import Like

router = APIRouter(prefix="/likes", tags=["Likes"])

@router.post("/{post_id}")
def like_post(
    post_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    existing = db.query(Like).filter(
        Like.post_id == post_id,
        Like.user_id == user.id
    ).first()

    if existing:
        raise HTTPException(400, "Already liked")

    like = Like(post_id=post_id, user_id=user.id)
    db.add(like)
    db.commit()

    return {"message": "Post liked"}

@router.delete("/{post_id}")
def unlike_post(
    post_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    like = db.query(Like).filter(
        Like.post_id == post_id,
        Like.user_id == user.id
    ).first()

    if not like:
        raise HTTPException(404, "Like not found")

    db.delete(like)
    db.commit()
    return {"message": "Post unliked"}
