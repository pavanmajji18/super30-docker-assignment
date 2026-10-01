# Task 16: Inter-Container Networking

## Commands

```bash
docker network create super30-net
docker run -d --network super30-net --name server-node nginx:alpine
docker run --rm --network super30-net alpine:latest ping -c 3 server-node
```
