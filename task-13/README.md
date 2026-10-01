# Task 13: Pass Runtime Environment Variables

## Commands

```bash
docker build -t super30-env-api .
docker run -d -p 8000:8000 -e APP_ENV=production --name task13-env super30-env-api
```
Access endpoint: [http://localhost:8000/config](http://localhost:8000/config) -> returns `{"environment": "production", ...}`
