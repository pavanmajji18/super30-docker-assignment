#!/bin/bash
# Task 13: Pass environment variable using -e flag
docker run -d -p 8000:8000 -e APP_ENV=production --name task13-env super30-api
# Access at http://localhost:8000/config
