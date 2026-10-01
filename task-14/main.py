import os
from fastapi import FastAPI

app = FastAPI(title="Task 14 Dotenv App")

@app.get("/config")
def get_config():
    return {
        "environment": os.getenv("APP_ENV", "local"),
        "db_host": os.getenv("DB_HOST", "localhost")
    }
