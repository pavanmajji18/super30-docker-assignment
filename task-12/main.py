from fastapi import FastAPI

app = FastAPI(title="Requirements.txt Installed Dependencies Demo")

@app.get("/")
def read_root():
    return {"status": "dependencies_installed"}
