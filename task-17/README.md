# Task 17: Containerized PostgreSQL Database

## Command

```bash
docker run -d \
  --name super30-postgres \
  --network super30-net \
  -e POSTGRES_DB=super30_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=adminpassword \
  -p 5432:5432 \
  postgres:16-alpine
```
