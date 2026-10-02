import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+psycopg2://admin:adminpassword@db:5432/super30_db"
)

# Connect retry logic for resilient container startup
engine = create_engine(DATABASE_URL)
for attempt in range(15):
    try:
        with engine.connect():
            break
    except Exception as e:
        if attempt == 14:
            raise e
        time.sleep(2)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
