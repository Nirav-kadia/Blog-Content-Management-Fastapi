# Quick Start Guide

Get the FastAPI Blog/CMS API running in 5 minutes!

## Prerequisites

- Python 3.11+
- PostgreSQL installed and running

## Quick Setup

### 1. Clone & Navigate

```bash
git clone https://github.com/YOUR_USERNAME/Blog_fastapi.git
cd Blog_fastapi
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Database

Open PostgreSQL and run:
```sql
CREATE DATABASE blog_db;
```

### 5. Configure Environment

Copy `.env.example` to `.env`:
```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Edit `.env` and update:
- `DATABASE_URL` with your PostgreSQL password
- `SECRET_KEY` with a secure random key

### 6. Create Admin User

```bash
python create_admin.py
```

### 7. Start Server

```bash
uvicorn app.main:app --reload
```

## Access Points

- **API Documentation:** http://127.0.0.1:8000/docs
- **Admin Panel:** http://127.0.0.1:8000/admin
- **API Base:** http://127.0.0.1:8000

## Default Admin Credentials

- **Email:** admin@example.com
- **Password:** admin123

⚠️ **Change this password immediately after first login!**

## Test the API

### 1. Register a User

Go to: http://127.0.0.1:8000/docs

1. Find `POST /auth/register`
2. Click "Try it out"
3. Enter:
```json
{
  "email": "test@example.com",
  "password": "testpass123"
}
```
4. Click "Execute"

### 2. Login

1. Find `POST /auth/login`
2. Click "Try it out"
3. Enter:
   - username: `test@example.com`
   - password: `testpass123`
4. Copy the `access_token` from response

### 3. Authorize

1. Click the "Authorize" button at the top
2. Enter: `Bearer YOUR_ACCESS_TOKEN`
3. Click "Authorize"

### 4. Create a Post

1. Find `POST /posts/`
2. Click "Try it out"
3. Enter:
```json
{
  "title": "My First Post",
  "content": "Hello World!",
  "status": "PUBLISHED"
}
```
4. Click "Execute"

### 5. View Posts

1. Find `GET /posts/`
2. Click "Try it out"
3. Click "Execute"
4. See your post!

## Using the Admin Panel

1. Go to: http://127.0.0.1:8000/admin
2. Click "Users" to manage users
3. Click "Posts" to manage posts
4. Click "Comments" to manage comments
5. Click "Likes" to view likes

## Common Issues

### Database Connection Error

```bash
# Check if PostgreSQL is running
# Windows
pg_ctl status

# macOS/Linux
sudo systemctl status postgresql
```

### Module Not Found

```bash
# Make sure virtual environment is activated
# Then reinstall
pip install -r requirements.txt
```

### Port Already in Use

```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [ADMIN_SETUP.md](ADMIN_SETUP.md) for admin panel details
- Explore the API at http://127.0.0.1:8000/docs

## Need Help?

- Check the [README.md](README.md) troubleshooting section
- Open an issue on GitHub
- Review the code comments in the source files

---

**You're all set! Happy coding! 🚀**
