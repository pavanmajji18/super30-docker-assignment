# Super 30 Docker Assignment

A structured multi-tier Docker assignment repository covering containerization fundamentals, networking, volumes, microservice health checks, and a production-grade 3-tier Student Management System built with **FastAPI**, **PostgreSQL**, and **Nginx**.

---

## 🛠️ Repository Architecture & Directory Structure

```text
super30-docker-assignment/
├── task-01/                   # Task 1: Pull and run interactive Ubuntu container
├── task-02/                   # Task 2: Install Python inside Ubuntu container & execute script
├── task-03/                   # Task 3: Custom container naming (super30-linux)
├── task-04/                   # Task 4: Detached mode, container lifecycle & removal
├── task-05/                   # Task 5: Pull multiple base images & list local image cache
├── task-06/                   # Task 6: Simple Python app containerization
├── task-07/                   # Task 7: Build & run custom image (super30-python-app)
├── task-08/                   # Task 8: FastAPI app containerization
├── task-09/                   # Task 9: FastAPI port binding on port 8000 (-p 8000:8000)
├── task-10/                   # Task 10: FastAPI port binding on host port 5000 (-p 5000:8000) & NAT explanation
├── task-11/                   # Task 11: Dockerfile instruction breakdown (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD)
├── task-12/                   # Task 12: Dependency management & layer caching with requirements.txt
├── task-13/                   # Task 13: Runtime environment variables (-e APP_ENV=production)
├── task-14/                   # Task 14: Environment configuration (.env, .env.example, .dockerignore)
├── task-15/                   # Task 15: Data persistence with named Docker volumes (super30-data)
├── task-16/                   # Task 16: Inter-container communication over custom bridge network (super30-net)
├── task-17/                   # Task 17: Containerized PostgreSQL with environment variables
├── task-18/                   # Task 18: FastAPI container connected to separate PostgreSQL container
├── task-19/                   # Task 19: Docker Compose orchestration (FastAPI → PostgreSQL)
├── task-20/                   # Task 20: 3-Tier Architecture (Nginx Frontend → FastAPI Backend → PostgreSQL DB)
├── task-21/                   # Task 21: Microservice health checks (/health endpoint & pg_isready)
├── task-22/                   # Task 22: REST CRUD application with persistent database storage
└── task-23/                   # Task 23: Final Challenge — Complete Student Management System
    ├── docker-compose.yml
    ├── .env.example
    ├── backend/               # FastAPI + SQLAlchemy + Pydantic backend
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── app/
    │       ├── main.py
    │       ├── database.py
    │       ├── models.py
    │       └── schemas.py
    └── frontend/              # Nginx + Glassmorphic UI frontend
        ├── Dockerfile
        ├── nginx.conf
        └── src/
            ├── index.html
            ├── styles.css
            └── app.js
```

---

## ⚡ Quick Start: Task 23 Student Management System

The flagship project in `task-23` deploys a complete 3-tier Student Management System microservices stack using Docker Compose.

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (v20+ or later) with Docker Compose installed.

### Launching the Stack

```bash
cd task-23
docker compose up --build -d
```

### Access Endpoints
* 🌐 **Frontend Web Portal**: [http://localhost:3000](http://localhost:3000)
* 📖 **FastAPI Interactive Docs (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)
* 🩺 **Backend Healthcheck**: [http://localhost:8000/health](http://localhost:8000/health)

---

## 🧪 Exercise Index & Running Individual Tasks

| Task | Topic | Directory | Execution Command |
| --- | --- | --- | --- |
| **01** | Interactive Ubuntu | `task-01/` | `bash task-01/commands.sh` |
| **02** | Install Python in Ubuntu | `task-02/` | `bash task-02/commands.sh` |
| **03** | Custom Container Name | `task-03/` | `bash task-03/commands.sh` |
| **04** | Container Lifecycle | `task-04/` | `bash task-04/commands.sh` |
| **05** | Image Cache & Pull | `task-05/` | `bash task-05/commands.sh` |
| **06** | Python App Dockerfile | `task-06/` | `cd task-06 && docker build -t py-app .` |
| **07** | Custom Image Build & Run | `task-07/` | `cd task-07 && bash run.sh` |
| **08** | FastAPI Containerization | `task-08/` | `cd task-08 && docker build -t api .` |
| **09** | Port Binding 8000 | `task-09/` | `cd task-09 && bash run.sh` |
| **10** | Host Port Mapping 5000 | `task-10/` | `cd task-10 && bash run.sh` |
| **11** | Dockerfile Breakdown | `task-11/` | See comments in `task-11/Dockerfile` |
| **12** | Automatic Dependencies | `task-12/` | `cd task-12 && docker build -t api-deps .` |
| **13** | Runtime Env Variables | `task-13/` | `cd task-13 && bash run.sh` |
| **14** | Dotenv File & Dockerignore | `task-14/` | `cd task-14 && bash run.sh` |
| **15** | Persistent Volumes | `task-15/` | `bash task-15/run.sh` |
| **16** | Bridge Networking | `task-16/` | `bash task-16/run.sh` |
| **17** | PostgreSQL Container | `task-17/` | `bash task-17/run.sh` |
| **18** | FastAPI + Postgres Bridge | `task-18/` | `cd task-18 && bash run.sh` |
| **19** | Docker Compose Stack | `task-19/` | `cd task-19 && docker compose up -d` |
| **20** | 3-Tier Microservices | `task-20/` | `cd task-20 && docker compose up -d` |
| **21** | Microservice Health Checks | `task-21/` | `cd task-21 && docker compose up -d` |
| **22** | Persistent REST CRUD API | `task-22/` | `cd task-22 && docker compose up -d` |
| **23** | Student Portal (Final) | `task-23/` | `cd task-23 && docker compose up --build -d` |

---

## 💾 Data Persistence Verification (Task 23)

To demonstrate zero data loss across container lifecycle resets:

1. Create a record via Web UI ([http://localhost:3000](http://localhost:3000)) or `curl`:
   ```bash
   curl -X POST http://localhost:8000/students \
     -H "Content-Type: application/json" \
     -d '{"full_name":"Pavan Kumar","email":"pavan@example.com","course":"Generative AI","enrollment_number":"STU-2026-001"}'
   ```
2. Stop and remove containers:
   ```bash
   docker compose down
   ```
3. Restart containers:
   ```bash
   docker compose up -d
   ```
4. Verify data persistence:
   ```bash
   curl http://localhost:8000/students
   ```

---

## 📄 License
MIT License. Open-source educational repository for Docker containerization practice.
