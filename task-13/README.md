# Task 13: Pass Runtime Environment Variables

## Command

```bash
docker run -d -p 8000:8000 -e APP_ENV=production --name task13-env super30-api
```
Access endpoint: [http://localhost:8000/config](http://localhost:8000/config) -> returns `{"environment": "production"}`
