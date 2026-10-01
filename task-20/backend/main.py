import os
from fastapi import FastAPI

app = FastAPI(title="Three Tier Backend API")

@app.get("/")
def read_root():
    return {"message": "Three-tier architecture backend active"}

@app.get("/health")
def health():
    return {"status": "healthy"}
