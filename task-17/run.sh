#!/bin/bash
# Task 17: Run PostgreSQL container with environment variables
docker network create super30-net 2>/dev/null || true
docker run -d \
  --name super30-postgres \
  --network super30-net \
  -e POSTGRES_DB=super30_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=adminpassword \
  -p 5432:5432 \
  postgres:16-alpine
