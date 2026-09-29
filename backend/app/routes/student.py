from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database import get_db
from ..models.student import Student
from ..services.resume_parser import ResumeParser

class SkillsUpdate(BaseModel):
    skills: list

router = APIRouter(prefix="/api/students", tags=["students"])

# Student create karo
@router.post("/create/")
def create_student(email: str, name: str, phone: str, db: Session = Depends(get_db)):
    new_student = Student(email=email, name=name, phone=phone)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student created successfully", "id": new_student.id}

# Student profile dekho
@router.get("/profile/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return {"error": "Student not found"}
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "skills": student.skills
    }

# Resume parse karo
@router.post("/parse-resume/")
def parse_resume(text: str):
    parsed = ResumeParser.parse_resume_text(text)
    return {"data": parsed}

# Sab students dekho
@router.get("/all/")
def get_all(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return {"total": len(students), "students": [{"id": s.id, "name": s.name, "email": s.email} for s in students]}

# Skills update karo
@router.put("/update-skills/{student_id}")
def update_skills(student_id: int, skills_data: SkillsUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return {"error": "Student not found"}
    student.skills = skills_data.skills
    db.commit()
    return {"message": "Skills updated", "skills": student.skills}