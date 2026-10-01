# Task 22: Persistent CRUD Application (FastAPI + PostgreSQL)

A complete RESTful CRUD API service with persistent database storage across container restarts.

## Endpoints

- **POST /items**: Create a new item record.
- **GET /items**: Retrieve all item records.
- **GET /items/{item_id}**: Retrieve a specific item by ID.
- **PUT /items/{item_id}**: Update an existing item by ID.
- **DELETE /items/{item_id}**: Delete an item by ID.

## Execution

```bash
docker compose up -d
```
