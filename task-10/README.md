# Task 10: Run FastAPI Image on Host Port 5000

## Command

```bash
docker run -d -p 5000:8000 --name api-port-5000 super30-api
```

Access via browser: [http://localhost:5000/docs](http://localhost:5000/docs)

Read `EXPLANATION.md` for a technical breakdown of Docker's port mapping (NAT) mechanism.
