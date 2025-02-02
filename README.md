
# Student Management System 🎓

[![Django](https://img.shields.io/badge/Django-3.2-green)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-blue)](https://tailwindcss.com/)

A modern web application for managing student records with full CRUD operations, built with Django and Tailwind CSS.


## Features ✨

**Core Functionality**
- ✅ Create, Read, Update, Delete (CRUD) student records
- 🔍 Search students by name, email, or phone number
- 🎚️ Filter students by course
- 📱 Responsive design for all devices

**User Interface**
- 🎨 Modern UI with Tailwind CSS
- 💡 Interactive forms with validation
- 📲 Responsive data tables
- 🚦 Success/error message notifications

**Security**
- 🔒 CSRF protection
- ✅ Form validation
- 🛡️ Secure delete confirmation


## Usage 🚀

**1. Add New Student**

- Click "Add Student" in navigation
- Fill form with student details
- Submit to save record

**2. Search Students**
- Use search bar at top
- Search by name, email, or phone

**3. Filter by Course**

- Select course from dropdown
- Automatically filters list

**4. Edit/Delete Students**

- Click action buttons in table
- Edit details or confirm deletion


## Technology Stack 💻

**Backend**
- Python 3.9+
- Django 3.2
- SQLite (Development)

**Frontend**
- Tailwind CSS 3.0
- HTML5
- Django Templates

**Tools**
- Django Widget Tweaks
- Icons8 (Icons)
## Project Structure 📂

**student-management-system/**
- ├── sms/                  # Django project config
- ├── students/             # Main application
- │   ├── migrations/       # Database migrations
- │   ├── templates/        # HTML templates
- │   ├── models.py         # Student model
- │   ├── views.py          # Class-based views
- │   └── urls.py           # Application URLs
- ├── db.sqlite3            # Database (dev)
- └── README.md             # Project Info
## Installation ⚙️

1. **Clone Repository**
```bash
git clone https://github.com/mdOmarfaruk151/Student-Management-System.git
cd student-management-system
```
2. **Set Up Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```
3. **Install Dependencies**
```bash
pip freeze > requirements.txt
```
4. **Create Superuser (Admin Setup)**
```bash
python manage.py createsuperuser
```
5. **Run Migrations**
```bash
python manage.py migrate
```
6. **Run Development Server**
 ```bash
 python manage.py runserver
 ```   
7. **Visit http://localhost:8000 in your browser.**
## Acknowledgments 🙏

 - [Icons by Icons8](https://icons8.com/)
 - [CSS Framework by Tailwind CSS](https://tailwindcss.com/docs/installation/using-vite)
 - [Django Documentation Team](https://docs.djangoproject.com/en/5.1/)
 - [Developed by Md. Omar Faruk](https://github.com/mdOmarfaruk151)

