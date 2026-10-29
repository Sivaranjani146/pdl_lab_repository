from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# PostgreSQL connection
DATABASE_URL = "postgresql://postgres:Aids@123@localhost:5432/oceanverse_db"


# Create database engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for database models
Base = declarative_base()


# Database connection function
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()