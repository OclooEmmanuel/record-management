# Record Management System

A full-stack Django web application for managing contact records, featuring both a traditional web interface and a REST API with JWT authentication.

🔗 **Live Demo**: [record-management-zeta.vercel.app](https://record-management-zeta.vercel.app)

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Django](https://img.shields.io/badge/django-4.x%2B-green)
![License](https://img.shields.io/github/license/OclooEmmanuel/record-management)
![Last Commit](https://img.shields.io/github/last-commit/OclooEmmanuel/record-management)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Web Routes](#web-routes)
- [API Documentation](#-api-documentation)
- [Authentication Flow](#-authentication-flow)
- [Database Models](#-database-models)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Overview

Record Management System is a full-featured Django application that demonstrates best practices for building RESTful APIs. It provides a secure, token-based authentication system and complete CRUD functionality for managing contact records through both a web interface and REST API.

Key Highlights:
- Production-ready code structure
- Secure JWT authentication with token blacklisting
- Interactive API documentation (Swagger UI)
- Clean separation of concerns between web views and API
- Easy to extend and customize

---

## ✨ Features

**🔐 Authentication**
- User registration with validation
- JWT token-based authentication
- Token refresh mechanism
- Secure logout with token blacklisting
- Password hashing with Django's built-in system

**📊 Record Management**
- Create, view, update, and delete records
- Search and filter records
- Proper error handling and status codes
- Protected routes (login required)

**🛡️ Security**
- JWT token expiration
- Token blacklisting on logout
- Protected endpoints requiring authentication

**🎨 User Interface**
- Clean, responsive HTML templates
- Bootstrap integration
- User-friendly forms for registration and login
- Dashboard-style record management interface

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Backend Framework | Django 6 | Web framework |
| API Framework | Django REST Framework | REST API construction |
| Authentication | Simple JWT | JWT token management |
| Database | SQLite (dev) / PostgreSQL (prod) | Data storage |
| Frontend | HTML, CSS, Bootstrap | User interface |
| API Docs | drf-yasg (Swagger) | Interactive API documentation |
| Language | Python 3.13 | - |

---

## 📁 Project Structure

```
record-management/
├── main/                       # Django project settings & root URLs
├── webapp/                     # Main application
│   ├── admin.py                # Admin interface configuration
│   ├── models.py               # Records model
│   ├── views.py                # Web views (register, login, dashboard, CRUD)
│   ├── api.py                  # REST API endpoints
│   ├── serializers.py          # DRF serializers
│   ├── forms.py                # Django forms
│   ├── urls.py                 # URL routing
│   └── templates/              # HTML templates
│       └── webapp/
│           ├── index.html
│           ├── register.html
│           ├── my-login.html
│           ├── dashboard.html
│           ├── create-record.html
│           ├── update-record.html
│           └── view-record.html
├── static/                     # Static files (CSS, JS)
├── manage.py
├── requirements.txt
├── test.py                     # API test script
└── .gitignore
```

---

## 🚦 Installation

### Prerequisites

- Python 3.8+
- pip
- Git
- Virtual environment (recommended)

### Step-by-Step

1. **Clone the repository:**
```bash
git clone https://github.com/OclooEmmanuel/record-management.git
cd record-management
```

2. **Create and activate a virtual environment:**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables** — create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create a superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Start the development server:**
```bash
python manage.py runserver
```

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000` | Main site |
| `http://127.0.0.1:8000/api/` | API root |
| `http://127.0.0.1:8000/admin/` | Admin panel |
| `http://127.0.0.1:8000/swagger/` | Swagger UI |

---

## Web Routes

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/register/` | Register a new user |
| `/my-login/` | Login |
| `/user-logout/` | Logout |
| `/dashboard/` | View all records (auth required) |
| `/create-record/` | Add a new record (auth required) |
| `/update-record/<pk>/` | Edit a record (auth required) |
| `/view-record/<pk>/` | View a single record (auth required) |
| `/delete-record/<pk>/` | Delete a record (auth required) |

---

## 📡 API Documentation

### Authentication Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/register/` | No | Register a new user |
| POST | `/api/login/` | No | Login and receive JWT tokens |
| POST | `/api/logout/` | Yes | Logout and blacklist refresh token |
| POST | `/api/token/refresh/` | No | Get a new access token |

### Record Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/api/records/` | Yes | Get all records |
| POST | `/api/records/` | Yes | Create a new record |
| GET | `/api/records/<id>/` | Yes | Get a single record |
| PUT | `/api/records/<id>/update/` | Yes | Update a record |
| DELETE | `/api/records/<id>/delete/` | Yes | Delete a record |

### Example Requests

**Register:**
```json
POST /api/register/
{
    "username": "johndoe",
    "password": "securepassword123",
    "email": "john@example.com"
}
```

**Login:**
```json
POST /api/login/
{
    "username": "johndoe",
    "password": "securepassword123"
}
```
Response:
```json
{
    "refresh": "eyJ0eXAiOiJKV1Qi...",
    "access": "eyJ0eXAiOiJKV1Qi..."
}
```

**Authenticated request:**
```
Authorization: Bearer <access_token>
```

**Refresh token:**
```json
POST /api/token/refresh/
{
    "refresh": "<refresh_token>"
}
```

### Swagger UI

To use Swagger at `http://localhost:8000/swagger/`:
1. Hit `POST /api/login/` and copy the `access` token
2. Click the **Authorize** button at the top
3. Enter `Bearer <your_access_token>`
4. All subsequent requests will include the token automatically

---

## 🔐 Authentication Flow

```
1. Register        → POST /api/register/
2. Login           → POST /api/login/       → receive access + refresh tokens
3. Make requests   → include access token in Authorization header
4. Token expires   → POST /api/token/refresh/ → get new access token
5. Logout          → POST /api/logout/      → refresh token blacklisted
```

---

## 🗄️ Database Models

### Records Model

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| first_name | CharField | First name |
| last_name | CharField | Last name |
| email | CharField | Email address |
| phone | CharField | Phone number |
| adress | CharField | Street address |
| province | CharField | Province |
| city | CharField | City |
| country | CharField | Country |
| creation_date | DateTimeField | Auto-set on creation |

---

## ⚙️ Configuration

### JWT Settings (`settings.py`)

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

### Environment Variables (`.env`)

```env
# Django
SECRET_KEY=your-super-secret-key
DEBUG=True

# Database (PostgreSQL for production)
DB_NAME=record_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Production Settings

```python
DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 🧪 Testing

```bash
# Run unit tests
python manage.py test webapp

# Run API test script
python test.py
```

---

## 📈 Future Enhancements

- Pagination for record lists
- File upload support
- Email verification and password reset
- Rate limiting
- API versioning
- Docker containerization
- CI/CD pipeline

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: brief description"`
4. Push: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👤 Author

**Ocloo Emmanuel**

- GitHub: [@OclooEmmanuel](https://github.com/OclooEmmanuel)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
