from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.models.user import UserRole

def require_admin(user=Depends(get_current_user)):
    if user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user

def is_owner_or_admin(resource_owner_id: int, user):
    return user.role == UserRole.ADMIN or resource_owner_id == user.id
