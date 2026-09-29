from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database ka path
DATABASE_URL = "sqlite:///./campus_placement.db"

# Engine bana
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session banao
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base - models inherit karenge
Base = declarative_base()

# Database connection function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()