# Task 14: Environment Variable Files (`.env`) & `.dockerignore`

## Commands

```bash
docker build -t super30-envfile-api .
docker run -d -p 8000:8000 --env-file .env.example --name task14-envfile super30-envfile-api
```
Security Best Practice: `.env` containing production secrets is excluded via `.gitignore` and `.dockerignore`.
