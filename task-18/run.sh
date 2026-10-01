#!/bin/bash
# Task 18: Connect FastAPI container to PostgreSQL container
docker network create super30-net 2>/dev/null || true
docker build -t super30-backend ./backend
docker run -d --network super30-net --name api-backend -p 8000:8000 super30-backend
