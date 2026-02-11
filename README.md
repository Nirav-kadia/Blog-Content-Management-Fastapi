# FastAPI Blog/CMS API with Admin Panel

A full-featured blog and content management system built with FastAPI, SQLAlchemy, PostgreSQL, and SQLAdmin. This project includes user authentication, post management, comments, likes, and a powerful admin panel.

## 🚀 Features

### Core Features
- ✅ **User Authentication** - JWT-based authentication with role-based access control (USER/ADMIN)
- ✅ **Blog Posts** - Create, read, update, delete posts with draft/published status
- ✅ **Comments** - Users can comment on posts
- ✅ **Likes** - Like system for posts
- ✅ **Image Upload** - Upload images for blog posts
- ✅ **Soft Delete** - Posts are soft-deleted (not permanently removed)
- ✅ **Admin Panel** - Full-featured admin interface with SQLAdmin

### Admin Panel Features
- 🔐 **User Management** - Create, edit, delete users with secure password hashing
- 📝 **Post Management** - Manage all blog posts
- 💬 **Comment Management** - Moderate comments
- ❤️ **Like Management** - View all likes
- 🔍 **Search & Filter** - Search and sort all entities
- 📊 **Dashboard** - Overview of all data

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+** - [Download Python](https://www.python.org/downloads/)
- **PostgreSQL** - [Download PostgreSQL](https://www.postgresql.org/download/)
- **Git** - [Download Git](https://git-scm.com/downloads)

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Blog_fastapi.git
cd Blog_fastapi
```

### Step 2: Create Virtual Environment

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

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up PostgreSQL Database

1. **Create a PostgreSQL database:**

```sql
CREATE DATABASE blog_db;
```

2. **Create a PostgreSQL user (optional):**

```sql
CREATE USER blog_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE blog_db TO blog_user;
```

### Step 5: Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/blog_db

# Security
SECRET_KEY=your-secret-key-here-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

**Important:** 
- Replace `your_password` with your PostgreSQL password
- Generate a secure SECRET_KEY (you can use: `openssl rand -hex 32`)

### Step 6: Create Database Tables

The application will automatically create tables on first run, but you can also use Alembic for migrations:

```bash
# Initialize Alembic (if not already done)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

### Step 7: Create Admin User

Run the admin creation script:

```bash
python create_admin.py
```

This creates an admin user with:
- **Email:** admin@example.com
- **Password:** admin123

⚠️ **Important:** Change this password after first login!

### Step 8: Start the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at:
- **API:** http://127.0.0.1:8000
- **API Docs:** http://127.0.0.1:8000/docs
- **Admin Panel:** http://127.0.0.1:8000/admin

## 📁 Project Structure

```
Blog_fastapi/
├── app/
│   ├── admin/
│   │   └── admin.py              # Admin panel configuration
│   ├── core/
│   │   ├── config.py             # Configuration settings
│   │   └── security.py           # Password hashing & JWT
│   ├── dependencies/
│   │   ├── auth.py               # Authentication dependencies
│   │   └── permissions.py        # Permission checks
│   ├── models/
│   │   ├── base.py               # Base model with timestamps
│   │   ├── user.py               # User model
│   │   ├── post.py               # Post model
│   │   ├── comment.py            # Comment model
│   │   ├── like.py               # Like model
│   │   └── __init__.py
│   ├── routers/
│   │   ├── auth.py               # Authentication routes
│   │   ├── posts.py              # Post routes
│   │   ├── comments.py           # Comment routes
│   │   └── likes.py              # Like routes
│   ├── schemas/
│   │   ├── auth.py               # Auth schemas (Pydantic)
│   │   ├── post.py               # Post schemas
│   │   ├── comment.py            # Comment schemas
│   │   └── like.py               # Like schemas
│   ├── database.py               # Database connection
│   └── main.py                   # FastAPI application
├── alembic/                      # Database migrations
├── uploads/                      # Uploaded files (auto-created)
├── venv/                         # Virtual environment
├── .env                          # Environment variables
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
├── create_admin.py               # Admin user creation script
├── ADMIN_SETUP.md               # Detailed admin setup guide
└── README.md                     # This file
```

## 🔌 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/register` | Register new user | No |
| POST | `/auth/login` | Login user | No |
| GET | `/auth/me` | Get current user | Yes |

### Posts

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/posts/` | Get all published posts | No |
| GET | `/posts/{id}` | Get single post | No |
| POST | `/posts/` | Create new post | Yes |
| PUT | `/posts/{id}` | Update post | Yes (Owner/Admin) |
| DELETE | `/posts/{id}` | Delete post | Yes (Owner/Admin) |
| POST | `/posts/{id}/upload-image` | Upload post image | Yes (Owner/Admin) |
| GET | `/posts/admin/all_post` | Get all posts (including drafts) | Yes (Admin) |

### Comments

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/comments/post/{post_id}` | Get post comments | No |
| POST | `/comments/` | Create comment | Yes |
| PUT | `/comments/{id}` | Update comment | Yes (Owner/Admin) |
| DELETE | `/comments/{id}` | Delete comment | Yes (Owner/Admin) |

### Likes

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/likes/` | Like a post | Yes |
| DELETE | `/likes/{post_id}` | Unlike a post | Yes |
| GET | `/likes/post/{post_id}` | Get post likes count | No |

## 📖 Usage Examples

### 1. Register a New User

```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### 2. Login

```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword123"
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Create a Post

```bash
curl -X POST "http://127.0.0.1:8000/posts/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "status": "PUBLISHED"
  }'
```

### 4. Get All Posts

```bash
curl -X GET "http://127.0.0.1:8000/posts/"
```

### 5. Add a Comment

```bash
curl -X POST "http://127.0.0.1:8000/comments/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "post_id": 1,
    "content": "Great post!"
  }'
```

### 6. Like a Post

```bash
curl -X POST "http://127.0.0.1:8000/likes/" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "post_id": 1
  }'
```

## 🔐 Admin Panel Usage

### Accessing the Admin Panel

1. Navigate to: http://127.0.0.1:8000/admin
2. The admin panel is currently open (no authentication required)
3. You can add authentication by following the guide in `ADMIN_SETUP.md`

### Managing Users

1. Click **"Users"** in the sidebar
2. Click **"Create"** to add a new user
3. Fill in the form:
   - Email: user@example.com
   - Password: (will be automatically hashed)
   - Role: USER or ADMIN
   - Active: Check to activate user
4. Click **"Save"**

### Managing Posts

1. Click **"Posts"** in the sidebar
2. View all posts (including drafts)
3. Edit or delete posts
4. Search posts by title or content

### Managing Comments & Likes

- Navigate to **"Comments"** or **"Likes"** sections
- View, edit, or delete entries
- Search and filter as needed

## 🔒 Security Features

### Password Security
- Passwords are hashed using **bcrypt** before storage
- Plain text passwords are never stored in the database
- Password hashing happens automatically in the admin panel

### JWT Authentication
- Secure token-based authentication
- Tokens expire after 60 minutes (configurable)
- Tokens include user ID and role

### Role-Based Access Control
- **USER** role: Can create posts, comments, likes
- **ADMIN** role: Full access to all resources
- Middleware checks permissions on protected routes

### SQL Injection Protection
- SQLAlchemy ORM prevents SQL injection
- Parameterized queries used throughout

## 🧪 Testing the API

### Using Swagger UI (Recommended)

1. Navigate to: http://127.0.0.1:8000/docs
2. Click **"Authorize"** button
3. Login to get a token
4. Enter token in format: `Bearer YOUR_TOKEN`
5. Test all endpoints interactively

### Using Postman

1. Import the API endpoints
2. Set up environment variables:
   - `base_url`: http://127.0.0.1:8000
   - `token`: Your JWT token
3. Use `{{base_url}}` and `{{token}}` in requests

## 📊 Database Schema

### Users Table
```sql
- id (Primary Key)
- email (Unique)
- hashed_password
- role (USER/ADMIN)
- is_active
- created_at
- updated_at
- is_deleted
```

### Posts Table
```sql
- id (Primary Key)
- title
- content
- status (DRAFT/PUBLISHED)
- author_id (Foreign Key → users.id)
- image (Optional)
- created_at
- updated_at
- is_deleted
```

### Comments Table
```sql
- id (Primary Key)
- content
- post_id (Foreign Key → posts.id)
- user_id (Foreign Key → users.id)
- created_at
- updated_at
- is_deleted
```

### Likes Table
```sql
- id (Primary Key)
- post_id (Foreign Key → posts.id)
- user_id (Foreign Key → users.id)
- created_at
- Unique constraint on (post_id, user_id)
```

## 🐛 Troubleshooting

### Issue: Database Connection Error

**Error:** `could not connect to server`

**Solution:**
1. Ensure PostgreSQL is running
2. Check DATABASE_URL in `.env` file
3. Verify database exists: `psql -U postgres -c "\l"`

### Issue: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
# Ensure virtual environment is activated
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Password Not Hashing in Admin

**Error:** Passwords stored as plain text

**Solution:**
1. Check `bcrypt` version: `pip show bcrypt`
2. Should be version 4.0.1
3. Reinstall if needed: `pip install bcrypt==4.0.1`

### Issue: Admin Panel Not Loading

**Error:** 404 at `/admin`

**Solution:**
1. Check `app/main.py` has `init_admin(app)`
2. Verify `sqladmin` is installed: `pip show sqladmin`
3. Restart the server

### Issue: Uploads Directory Error

**Error:** `Directory 'uploads' does not exist`

**Solution:**
The app should auto-create this directory. If not:
```bash
mkdir uploads
mkdir uploads/posts
```

## 🚀 Deployment

### Deploying to Production

1. **Set Environment Variables:**
   - Use strong SECRET_KEY
   - Update DATABASE_URL for production database
   - Set `DEBUG=False`

2. **Use Production Server:**
   ```bash
   pip install gunicorn
   gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

3. **Set Up Reverse Proxy (Nginx):**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

4. **Enable HTTPS:**
   - Use Let's Encrypt for free SSL certificates
   - Configure Nginx for HTTPS

5. **Database Migrations:**
   ```bash
   alembic upgrade head
   ```

## 📝 Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/blog_db` |
| `SECRET_KEY` | JWT secret key | `your-secret-key-here` |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | `60` |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Your Name** - Initial work - [YourGitHub](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [SQLAdmin](https://aminalaee.dev/sqladmin/) - Admin panel for FastAPI
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [PostgreSQL](https://www.postgresql.org/) - Database

## 📞 Support

If you have any questions or issues:

1. Check the [ADMIN_SETUP.md](ADMIN_SETUP.md) for detailed admin panel guide
2. Open an issue on GitHub
3. Contact: your.email@example.com

## 🔄 Changelog

### Version 1.0.0 (2026-02-11)
- Initial release
- User authentication with JWT
- Blog post CRUD operations
- Comments and likes functionality
- Admin panel with SQLAdmin
- Image upload support
- Soft delete implementation

---

**Happy Coding! 🚀**
