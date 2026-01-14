FastAPI User Management System
A complete, production-ready CRUD (Create, Read, Update, Delete) application built with FastAPI, featuring a modern web interface and RESTful API.

https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white

✨ Features
Core CRUD Operations
✅ User Creation: Register new users with secure password hashing

✅ User Listing: View all users in a responsive table with pagination

✅ User Editing: Update user information with validation

✅ User Deletion: Remove users with confirmation dialogs

Security
🔐 Bcrypt Password Hashing: Secure password storage

📧 Email Validation: Proper email format validation

👤 Username Validation: Alphanumeric and underscore only

🔒 Form Validation: Server-side and client-side validation

User Interface
🎨 Modern Bootstrap 5 Design: Clean, responsive interface

📱 Mobile Responsive: Works on all device sizes

⚡ Real-time Feedback: Instant form validation and error messages

🎯 User Experience: Intuitive navigation and clear actions

Technical Features
🚀 FastAPI Backend: High-performance Python web framework

🗄️ SQLAlchemy ORM: Database abstraction layer

📊 SQLite Database: Lightweight, file-based database

📝 Jinja2 Templates: Server-side rendering

🔄 Auto-reload: Development server with hot reload

📋 Prerequisites
Python 3.8 or higher

pip (Python package manager)

Git (for version control)

🚀 Quick Start
1. Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/fastapi-rnd.git
cd fastapi-rnd
2. Set Up Virtual Environment
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the Application
bash
uvicorn app.main:app --reload

📁 Project Structure
text
fastapi-rnd/
├── app/                           # Application package
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # FastAPI application & routes
│   ├── database.py               # Database configuration
│   ├── models.py                 # SQLAlchemy models
│   ├── schemas.py                # Pydantic schemas
│   ├── crud.py                   # CRUD operations
│   └── templates/                # HTML templates
│       ├── base.html            # Base template
│       ├── users.html           # Users listing page
│       ├── create.html          # Create user form
│       ├── edit.html            # Edit user form
│       └── error.html           # Error page
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file

🔧 Configuration
Database
Type: SQLite

File: app.db (auto-created on first run)

Location: Project root directory

Security
Password Hashing: Bcrypt with 12 rounds

Validation: Pydantic schemas with custom validators

Input Sanitization: Built-in FastAPI validation

🌐 API Endpoints
Web Interface
Method	Endpoint	Description
GET	/	Redirects to /users
GET	/users	Display all users
GET	/create	Show create user form
POST	/create	Create new user
GET	/edit/{id}	Show edit user form
POST	/edit/{id}	Update user
GET	/delete/{id}	Delete user (web)
REST API
Method	Endpoint	Description
DELETE	/api/users/{id}	Delete user (API)

🧪 Testing the Application
Create a new user:

Navigate to /create

Fill in the form with test data

Submit and verify user appears in the list

Edit a user:

Click "Edit" on any user

Modify information

Submit and verify changes

Delete a user:

Click "Delete" on any user

Confirm the deletion

Verify user is removed from list
