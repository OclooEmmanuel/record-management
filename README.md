# Record Management System

A full-stack Django web application for managing records with a REST API built with Django REST Framework.

🔗 **Live Demo**: [record-management-zeta.vercel.app](https://record-management-zeta.vercel.app)

---

## Features

- User registration and authentication
- Create, read, update, and delete records
- REST API with JWT authentication
- Swagger API documentation
- Search and filter records

---

## Tech Stack

- **Backend**: Django 6, Django REST Framework
- **Authentication**: SimpleJWT
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap
- **API Docs**: drf-yasg (Swagger)

---

## Project Structure

```
record-management/
├── main/           # Django project settings
├── webapp/         # Main application
│   ├── models.py       # Records model
│   ├── views.py        # Web views
│   ├── api.py          # API endpoints
│   ├── serializers.py  # DRF serializers
│   ├── forms.py        # Django forms
│   └── urls.py         # URL routing
├── static/         # Static files
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/OclooEmmanuel/record-management.git
cd record-management
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000`

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register a new user |
| POST | `/api/login/` | Login and get JWT tokens |
| POST | `/api/logout/` | Logout and blacklist token |
| POST | `/api/token/refresh/` | Refresh access token |

### Records

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/records/` | Get all records |
| POST | `/api/records/` | Create a new record |
| GET | `/api/records/<id>/` | Get a single record |
| PUT | `/api/records/<id>/update/` | Update a record |
| DELETE | `/api/records/<id>/delete/` | Delete a record |

### Authentication

All record endpoints require a valid JWT access token in the request header:

```
Authorization: Bearer <access_token>
```

---

## API Documentation

Swagger UI is available at:
```
http://localhost:8000/swagger/
```

---

## License

This project is licensed under the MIT License.
