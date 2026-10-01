#!/bin/bash
# Task 14: Load environment variables via --env-file
docker run -d -p 8000:8000 --env-file .env.example --name task14-envfile super30-api
