
📊 Data Dashboard - داشبورد مدیریت دیتاست
English Version
Project Overview
Developer: Fariborz Zamani
Email: fariborz499@gmail.com
Technology Stack: Django 4.2, Python, Bootstrap 5, SQLite, Pandas

What is this project?
A powerful web-based dashboard for managing Excel datasets. Users can upload Excel files, store them in a database, and access them via web interface or REST API.

Key Features:
✅ Upload Excel files (.xlsx, .xls)

✅ Automatic data extraction and storage

✅ User authentication and authorization

✅ List, view, and delete datasets

✅ Pagination for large datasets

✅ Responsive UI with Bootstrap 5

✅ REST API for programmatic access

✅ Persian (Farsi) language support

✅ File size validation (max 10MB)

✅ Secure file handling

API Endpoints:
Method	Endpoint	Description
GET	/api/datasets/	Get all datasets
GET	/api/datasets/<id>/	Get specific dataset
POST	/api/upload/	Upload new Excel file
Installation & Setup:
bash
# Clone the project
git clone [your-repo-url]

# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Install dependencies
pip install django pandas openpyxl crispy-forms crispy-bootstrap5

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
Access Points:
Web App: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

API Documentation: http://127.0.0.1:8000/api-setup/

Use Cases:
Data Analysts: Store and manage multiple Excel datasets

Organizations: Centralized data storage system

Developers: Integrate with other apps via REST API

Researchers: Manage research data efficiently

