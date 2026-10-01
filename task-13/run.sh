#!/bin/bash
# Task 13: Build dedicated image with /config endpoint and pass environment variable
docker build -t super30-env-api .
docker run -d -p 8000:8000 -e APP_ENV=production --name task13-env super30-env-api
# Access at http://localhost:8000/config
