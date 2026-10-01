from fastapi import FastAPI, status

app = FastAPI(title="Healthchecked API")

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy", "service": "backend"}

@app.get("/")
def read_root():
    return {"message": "Service is healthy and responding"}
