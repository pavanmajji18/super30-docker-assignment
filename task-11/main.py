from fastapi import FastAPI

app = FastAPI(title="Production Dockerfile Demo")

@app.get("/")
def read_root():
    return {"status": "running"}
