# Job Board API

A RESTful API for a job board application built with Django and Django REST Framework (DRF).  
It supports JWT authentication, custom user roles (employer/job seeker), secure registration, and PostgreSQL integration.

---

## Features

- Custom user model with role-based access (`is_employer`, `is_job_seeker`)  
- User registration with email validation and password security  
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
