# Campus Placement AI System

AI-powered intelligent campus placement platform

## Tech Stack
- Backend: FastAPI, SQLAlchemy, SQLite
- API: REST with Swagger documentation
- Language: Python 3.10+

## Features
- Resume parsing & skill extraction
- Student profile management
- Job matching system
- Resume analysis

## Installation

1. Create virtual environment: `python -m venv venv`
2. Activate: `venv\Scripts\activate`
3. Install packages: `pip install -r requirements.txt`
4. Run server: `uvicorn backend.app.main:app --reload`
5. Open: http://localhost:8000/docs

## API Endpoints

- `POST /api/students/create/` - Create student
- `GET /api/students/profile/{id}` - Get student profile
- `POST /api/students/parse-resume/` - Parse resume
- `GET /api/students/all/` - Get all students

## Author
Payal Sharma | B.Tech AI, CIET Raipur