import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="FastAPI + PostgreSQL Integration")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:adminpassword@super30-postgres:5432/super30_db"
)

@app.get("/")
def read_root():
    return {"message": "FastAPI connected to separate PostgreSQL container"}

@app.get("/db-check")
def db_check():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            return {"status": "connected", "postgres_version": result.scalar()}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
