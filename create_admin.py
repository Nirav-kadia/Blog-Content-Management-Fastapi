"""
Script to create an admin user for the blog application.

Usage:
    python create_admin.py
"""

from sqlalchemy.orm import Session
from app.database import engine
from app.models.user import User, UserRole
from app.core.security import hash_password


def create_admin():
    """Create an admin user if one doesn't exist"""
    
    with Session(engine) as session:
        # Check if admin already exists
        existing_admin = session.query(User).filter(
            User.email == "admin@example.com"
        ).first()
        
        if existing_admin:
            print("❌ Admin user already exists!")
            print(f"   Email: {existing_admin.email}")
            print(f"   Role: {existing_admin.role}")
            return
        
        # Create admin user
        admin_user = User(
            email="admin@example.com",
            hashed_password=hash_password("admin123"),
            role=UserRole.ADMIN,
            is_active=True
        )
        
        session.add(admin_user)
        session.commit()
        
        print("✅ Admin user created successfully!")
        print("=" * 50)
        print("   Email:    admin@example.com")
        print("   Password: admin123")
        print("=" * 50)
        print("⚠️  Please change the password after first login!")


if __name__ == "__main__":
    create_admin()
