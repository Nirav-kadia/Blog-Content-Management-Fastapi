from pydantic import BaseModel
from typing import Optional
from app.models.post import PostStatus

# Base schema (shared fields)
class PostBase(BaseModel):
    title: str
    content: str

# Create post
class PostCreate(PostBase):
    status: PostStatus = PostStatus.DRAFT

# Update post
class PostUpdate(PostBase):
    status: PostStatus

# Response schema (optional but good practice)
class PostResponse(PostBase):
    id: int
    status: PostStatus
    author_id: int
    image: str | None = None

    class Config:
        from_attributes = True
