#!/bin/bash
# Task 9: Run FastAPI container on port 8000
docker build -t super30-api .
docker run -d -p 8000:8000 --name api-port-8000 super30-api
# Access at http://localhost:8000/docs
