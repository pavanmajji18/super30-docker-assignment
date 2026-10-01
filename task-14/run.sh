#!/bin/bash
# Task 14: Build dedicated image with /config endpoint and load environment variables via --env-file
docker build -t super30-envfile-api .
docker run -d -p 8000:8000 --env-file .env.example --name task14-envfile super30-envfile-api
# Access at http://localhost:8000/config
