import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get DB URL from environment (BEST PRACTICE)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:Anurag%402003@db:5432/reviews"
)

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # prevents stale connection errors
    echo=False
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()


# Dependency (VERY IMPORTANT for FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()