# Contributing to FastAPI Blog/CMS API

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear title** - Describe the bug briefly
2. **Description** - Detailed explanation of the issue
3. **Steps to reproduce** - How to recreate the bug
4. **Expected behavior** - What should happen
5. **Actual behavior** - What actually happens
6. **Environment** - OS, Python version, etc.
7. **Screenshots** - If applicable

**Example:**
```
Title: Password not hashing in admin panel

Description: When creating a user through the admin panel, 
the password is stored as plain text instead of being hashed.

Steps to reproduce:
1. Go to /admin
2. Click Users > Create
3. Enter email and password
4. Save
5. Check database - password is plain text

Expected: Password should be hashed
Actual: Password is stored as plain text

Environment: Windows 11, Python 3.11, PostgreSQL 14
```

### Suggesting Features

For feature requests, create an issue with:

1. **Feature description** - What you want to add
2. **Use case** - Why this feature is needed
3. **Proposed solution** - How it could be implemented
4. **Alternatives** - Other ways to achieve the same goal

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: Feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

## 📝 Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) style guide:

- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter)
- Use descriptive variable names
- Add docstrings to functions and classes

**Example:**
```python
def create_user(email: str, password: str) -> User:
    """
    Create a new user with hashed password.
    
    Args:
        email: User's email address
        password: Plain text password
        
    Returns:
        User: Created user object
        
    Raises:
        ValueError: If email already exists
    """
    # Implementation
    pass
```

### Code Organization

- **Models** - Database models in `app/models/`
- **Schemas** - Pydantic schemas in `app/schemas/`
- **Routers** - API routes in `app/routers/`
- **Dependencies** - Reusable dependencies in `app/dependencies/`
- **Core** - Core functionality in `app/core/`

### Naming Conventions

- **Files:** lowercase with underscores (`user_model.py`)
- **Classes:** PascalCase (`UserModel`)
- **Functions:** snake_case (`get_user_by_id`)
- **Constants:** UPPERCASE (`SECRET_KEY`)
- **Variables:** snake_case (`user_email`)

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

### Writing Tests

Create tests in `tests/` directory:

```python
# tests/test_auth.py
def test_register_user(client):
    """Test user registration"""
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpass123"}
    )
    assert response.status_code == 201
    assert "id" in response.json()
```

## 📚 Documentation

### Code Comments

- Add comments for complex logic
- Explain "why" not "what"
- Keep comments up to date

**Good:**
```python
# Hash password before storing to prevent plain text exposure
hashed_password = hash_password(password)
```

**Bad:**
```python
# Hash the password
hashed_password = hash_password(password)
```

### Docstrings

Use Google-style docstrings:

```python
def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Retrieve a user by email address.
    
    Args:
        db: Database session
        email: User's email address
        
    Returns:
        User object if found, None otherwise
        
    Example:
        >>> user = get_user_by_email(db, "user@example.com")
        >>> print(user.email)
        user@example.com
    """
    return db.query(User).filter(User.email == email).first()
```

## 🔄 Git Workflow

### Commit Messages

Use conventional commits format:

```
<type>: <description>

[optional body]

[optional footer]
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

**Examples:**
```
feat: Add user profile endpoint

Add GET /users/me endpoint to retrieve current user profile.
Includes email, role, and creation date.

Closes #123
```

```
fix: Password hashing in admin panel

Fixed issue where passwords were stored as plain text
when creating users through the admin panel.

Fixes #456
```

### Branch Naming

- `feature/` - New features (`feature/user-profile`)
- `fix/` - Bug fixes (`fix/password-hashing`)
- `docs/` - Documentation (`docs/api-guide`)
- `refactor/` - Code refactoring (`refactor/auth-logic`)

## 🚀 Development Setup

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/Blog_fastapi.git
cd Blog_fastapi
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If exists
```

### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature
```

### 4. Make Changes

- Write code
- Add tests
- Update documentation

### 5. Test Changes

```bash
pytest
```

### 6. Commit and Push

```bash
git add .
git commit -m "feat: Your feature description"
git push origin feature/your-feature
```

### 7. Create Pull Request

- Go to GitHub
- Click "New Pull Request"
- Fill in the template
- Submit for review

## 📋 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] PR description explains changes

## 🔍 Code Review Process

1. **Automated checks** - CI/CD runs tests
2. **Maintainer review** - Code is reviewed
3. **Feedback** - Changes may be requested
4. **Approval** - PR is approved
5. **Merge** - Code is merged to main

## 🎯 Areas for Contribution

### High Priority

- [ ] Add unit tests for all endpoints
- [ ] Add integration tests
- [ ] Implement admin authentication
- [ ] Add email verification
- [ ] Add password reset functionality
- [ ] Implement rate limiting
- [ ] Add API versioning

### Medium Priority

- [ ] Add user profile endpoints
- [ ] Implement post categories/tags
- [ ] Add search functionality
- [ ] Implement pagination
- [ ] Add post scheduling
- [ ] Add rich text editor support

### Low Priority

- [ ] Add social media sharing
- [ ] Implement notifications
- [ ] Add analytics dashboard
- [ ] Multi-language support
- [ ] Dark mode for admin panel

## 💡 Tips for Contributors

### Good First Issues

Look for issues labeled `good first issue` - these are:
- Well-defined
- Limited in scope
- Good for beginners
- Have clear acceptance criteria

### Getting Help

- **Questions?** Open a discussion on GitHub
- **Stuck?** Comment on the issue
- **Need clarification?** Ask in the PR

### Best Practices

1. **Start small** - Begin with small contributions
2. **One feature per PR** - Keep PRs focused
3. **Test thoroughly** - Test your changes
4. **Document changes** - Update docs
5. **Be patient** - Reviews take time
6. **Be respectful** - Follow code of conduct

## 📞 Contact

- **GitHub Issues:** For bugs and features
- **GitHub Discussions:** For questions
- **Email:** your.email@example.com

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🎉**
