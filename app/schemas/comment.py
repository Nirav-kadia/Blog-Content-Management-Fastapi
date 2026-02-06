from pydantic import BaseModel

class CommentCreate(BaseModel):
    post_id: int
    content: str

class CommentResponse(BaseModel):
    id: int
    content: str
    post_id: int
    user_id: int

    class Config:
        from_attributes = True
