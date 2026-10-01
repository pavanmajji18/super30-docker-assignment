import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://admin:adminpassword@db:5432/super30_db"
)

# Connect retry logic for resilient container startup
engine = None
for attempt in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect():
            break
    except Exception:
        time.sleep(2)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
