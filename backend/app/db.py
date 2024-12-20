from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# loading environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# engine SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for model
Base = declarative_base()


# Dependency for creating a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
