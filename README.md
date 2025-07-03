# Job Board API

A RESTful API for a job board application built with Django and Django REST Framework (DRF).  
It supports JWT authentication, custom user roles (employer/job seeker), secure registration, and PostgreSQL integration.

---

## Features

- Custom user model with role-based access (`is_employer`, `is_job_seeker`)  
- User registration with email validation and password security  
- Job seekers can submit applications to jobs by uploading resumes and optionally adding cover letters.
- Each application tracks its status (e.g., applied, withdrawn, accepted, rejected).
- Employers can view and manage applications for their posted jobs.
- Role-based access controls ensure only authorized users (job seekers or employers) can perform actions on applications.
- Application status updates are securely handled with permission checks.
- Resume files are securely stored and accessible only to relevant users.
- Application data integrates with user and job models for full traceability.
- Error handling is consistent with the rest of the API for smooth client experience.
- JWT token-based authentication and authorization  
- CRUD operations for users and jobs (can be extended)  
- Environment variable management with `python-decouple`  
- PostgreSQL database backend  

---

## Tech Stack

- Python 3.x  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- Simple JWT (for JWT auth)  
- python-decouple (for environment variables)  

---

## Getting Started

### Prerequisites

- Python 3.x  
- PostgreSQL installed and running  

### Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/job-board-api.git
   cd job-board-api

2. Create and activate a virtual environment 
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate     # On Windows

3. Install dependencies 
   ```bash
   pip install -r requirements.txt

4. Create a .env file in the root directory and configure your environment variables (use .env.example as reference):  
   ```bash
    SECRET_KEY=your_django_secret_key_here
    DEBUG=True
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=your_db_name
    DB_USERNAME=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432

5. Apply migrations
   ```bash
   python manage.py migrate

6. Run the development server
   ```bash
   python manage.py runserver

## Postman Collection
   To make testing and exploring the Job Board API easier, I have included a Postman collection in the project repository under the postman/ folder.
