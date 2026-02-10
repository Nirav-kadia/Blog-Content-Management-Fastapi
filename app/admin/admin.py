"""
SQLAdmin Configuration for FastAPI Blog Application

This module sets up the admin panel with proper password hashing
for user management and CRUD operations for all models.
"""

from fastapi import FastAPI
from sqladmin import Admin, ModelView
from starlette.requests import Request
from wtforms import Form, StringField, BooleanField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Optional as OptionalValidator

from app.database import engine
from app.models.user import User, UserRole
from app.models.post import Post
from app.models.comment import Comment
from app.models.like import Like
from app.core.security import hash_password


# Custom form for User with password field
class UserForm(Form):
    """Custom form for User model that includes password field"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[OptionalValidator()])
    role = SelectField('Role', choices=[('USER', 'User'), ('ADMIN', 'Admin')])
    is_active = BooleanField('Active')


class UserAdmin(ModelView, model=User):
    """Admin view for User model with password hashing"""
    
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"
    
    # Use custom form
    form = UserForm
    
    # Columns to display in list view
    column_list = [User.id, User.email, User.role, User.is_active, User.created_at]
    
    # Searchable columns
    column_searchable_list = [User.email]
    
    # Sortable columns
    column_sortable_list = [User.id, User.email, User.created_at]
    
    # Default sort
    column_default_sort = [(User.created_at, True)]
    
    # Permissions
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    
    async def insert_model(self, request: Request, data: dict) -> User:
        """
        Override insert to hash password before saving.
        This is called when creating a new user.
        """
        # Get password from form
        form_data = await request.form()
        password = form_data.get("password", "")
        
        print(f"DEBUG - Form data keys: {list(form_data.keys())}")
        print(f"DEBUG - Password value: {'[PROVIDED]' if password else '[EMPTY]'}")
        print(f"DEBUG - Data dict: {data}")
        
        if not password:
            raise ValueError("Password is required when creating a new user")
        
        # Hash password and add to data
        data["hashed_password"] = hash_password(password)
        
        # Remove password from data (it's not a real column)
        data.pop("password", None)
        
        # Save user
        return await super().insert_model(request, data)
    
    async def update_model(self, request: Request, pk: str, data: dict) -> User:
        """
        Override update to hash password if provided.
        This is called when editing an existing user.
        """
        # Get password from form
        form_data = await request.form()
        password = form_data.get("password", "")
        
        # Only update password if a new one is provided
        if password:
            data["hashed_password"] = hash_password(password)
        
        # Remove password from data (it's not a real column)
        data.pop("password", None)
        
        # Update user
        return await super().update_model(request, pk, data)


class PostAdmin(ModelView, model=Post):
    """Admin view for Post model"""
    
    name = "Post"
    name_plural = "Posts"
    icon = "fa-solid fa-newspaper"
    
    column_list = [Post.id, Post.title, Post.author_id, Post.created_at, Post.updated_at]
    column_searchable_list = [Post.title, Post.content]
    column_sortable_list = [Post.id, Post.created_at, Post.updated_at]
    column_default_sort = [(Post.created_at, True)]
    
    # Exclude relationships from forms
    form_excluded_columns = [Post.comments, Post.likes]
    
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class CommentAdmin(ModelView, model=Comment):
    """Admin view for Comment model"""
    
    name = "Comment"
    name_plural = "Comments"
    icon = "fa-solid fa-comment"
    
    column_list = [Comment.id, Comment.content, Comment.post_id, Comment.user_id, Comment.created_at]
    column_searchable_list = [Comment.content]
    column_sortable_list = [Comment.id, Comment.created_at]
    column_default_sort = [(Comment.created_at, True)]
    
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class LikeAdmin(ModelView, model=Like):
    """Admin view for Like model"""
    
    name = "Like"
    name_plural = "Likes"
    icon = "fa-solid fa-heart"
    
    column_list = [Like.id, Like.post_id, Like.user_id, Like.created_at]
    column_sortable_list = [Like.id, Like.created_at]
    column_default_sort = [(Like.created_at, True)]
    
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


def init_admin(app: FastAPI) -> Admin:
    """
    Initialize and configure the admin panel.
    
    Args:
        app: FastAPI application instance
        
    Returns:
        Admin: Configured admin instance
    """
    # Create admin instance
    admin = Admin(
        app=app,
        engine=engine,
        title="Blog Admin Panel",
        base_url="/admin"
    )
    
    # Register all model views
    admin.add_view(UserAdmin)
    admin.add_view(PostAdmin)
    admin.add_view(CommentAdmin)
    admin.add_view(LikeAdmin)
    
    return admin
