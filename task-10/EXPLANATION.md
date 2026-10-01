# Why Port 5000 Works: Port Mapping & NAT Explanation

## Syntax breakdown
```bash
docker run -p <Host_Port>:<Container_Port> super30-api
```
When running `docker run -p 5000:8000 super30-api`:

1. **Inside the container**: The Uvicorn server is listening on `0.0.0.0:8000` inside its isolated network namespace.
2. **On the host machine**: Docker Daemon creates a proxy / NAT (Network Address Translation) rule via `docker-proxy` / iptables that binds host port `5000`.
3. **Traffic Flow**: When you navigate to `http://localhost:5000`, the host routes TCP packets on port `5000` directly to port `8000` inside the container.
