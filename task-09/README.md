# Task 9: Run FastAPI Container on Port 8000

## Command

```bash
docker build -t super30-api .
docker run -d -p 8000:8000 --name api-port-8000 super30-api
```

Access via browser: [http://localhost:8000/docs](http://localhost:8000/docs)
