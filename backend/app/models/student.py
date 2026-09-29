from sqlalchemy import Column, Integer, String, Text, Float, DateTime, JSON
from sqlalchemy.sql import func
from ..database import Base

# Student ka data structure
class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    phone = Column(String)
    gpa = Column(Float, default=0.0)
    skills = Column(JSON, default=[])
    resume_text = Column(Text, default="")
    created_at = Column(DateTime, server_default=func.now())

# Job ka data structure
class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    title = Column(String)
    description = Column(Text)
    skills_required = Column(JSON, default=[])
    salary_range = Column(String)

# Student-Job match ka record
class JobMatch(Base):
    __tablename__ = "job_matches"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    job_id = Column(Integer)
    match_score = Column(Float)