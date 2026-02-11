from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class PostStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True, nullable=False)
    content = Column(Text, nullable=False)
    status = Column(Enum(PostStatus), default=PostStatus.DRAFT)
    image = Column(String, nullable=True)

    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("Like", back_populates="post")
