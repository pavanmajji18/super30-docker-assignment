from fastapi import FastAPI

app = FastAPI(title="Super30 API")

@app.get("/")
def read_root():
    return {"status": "running", "platform": "Docker Container"}
