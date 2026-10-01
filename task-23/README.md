# Task 23: Complete Student Management System (Final Project)

An enterprise 3-tier microservices application fully containerized using Docker and orchestrated with Docker Compose.

## Architecture Components

1. **Frontend Tier (Nginx:Alpine)**
   - Port: `3000` (mapped to container port `80`)
   - Serves static Web UI with Glassmorphic styling, real-time search, stats dashboard, and CRUD management.

2. **Backend Tier (FastAPI + SQLAlchemy)**
   - Port: `8000` (mapped to container port `8000`)
   - Provides RESTful APIs for student management with interactive OpenAPI documentation at `/docs`. Includes health check endpoint at `/health`.

3. **Database Tier (PostgreSQL 16 Alpine)**
   - Port: `5432` (mapped to container port `5432`)
   - Uses named Docker volume `postgres_data` for persistent record storage across container lifecycles.

## Quick Start Command

```bash
docker compose up --build -d
```

## Access Points
- **Frontend Dashboard**: [http://localhost:3000](http://localhost:3000)
- **FastAPI OpenAPI Swagger**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Backend Health Check**: [http://localhost:8000/health](http://localhost:8000/health)
