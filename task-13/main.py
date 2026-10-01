import os
from fastapi import FastAPI

app = FastAPI(title="Task 13 Env App")

@app.get("/config")
def get_config():
    env_name = os.getenv("APP_ENV", "local")
    return {"environment": env_name}
