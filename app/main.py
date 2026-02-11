from fastapi import FastAPI
from app.database import engine
from app.models.base import Base
from app.admin.admin import init_admin
from fastapi.staticfiles import StaticFiles
import os

# Import models so SQLAlchemy knows them
from app.models import user, post, comment, like

# Routers
from app.routers import auth, posts, comments, likes

app = FastAPI(title="Blog / CMS API")

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize admin panel
init_admin(app)

# Include routers
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

# Create uploads directory if it doesn't exist
uploads_dir = "uploads"
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)
    os.makedirs(os.path.join(uploads_dir, "posts"))

# Mount static files for uploads
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

