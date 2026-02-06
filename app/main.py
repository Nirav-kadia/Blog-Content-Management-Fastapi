from fastapi import FastAPI
from app.database import engine
from app.models.base import Base

# Import models so SQLAlchemy knows them
from app.models import user, post, comment, like

# Routers
from app.routers import auth, posts, comments, likes

app = FastAPI(title="Blog / CMS API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

