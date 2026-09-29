from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .models.student import Student, Job, JobMatch
from .routes import student

# Database tables banao
Base.metadata.create_all(bind=engine)

# FastAPI app initialize
app = FastAPI(
    title="Campus Placement AI API",
    description="AI system for campus placements",
    version="1.0.0"
)

# CORS enable (frontend se access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes include karo
app.include_router(student.router)

# Basic endpoints
@app.get("/")
def read_root():
    return {"message": "Campus Placement AI Running!", "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}