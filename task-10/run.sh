#!/bin/bash
# Task 10: Run FastAPI Docker image on host port 5000 mapped to container port 8000
docker run -d -p 5000:8000 --name api-port-5000 super30-api
# Access via browser: http://localhost:5000/docs
