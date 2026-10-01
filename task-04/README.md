# Task 4: Detached Mode, Lifecycle & Removal

## Commands

```bash
# 1. Run in background detached mode (-d)
docker run -d --name super30-detached ubuntu:latest sleep 3600

# 2. Verify running container
docker ps --filter "name=super30-detached"

# 3. Stop and restart container
docker stop super30-detached
docker restart super30-detached

# 4. Stop and clean remove container
docker stop super30-detached
docker rm super30-detached
```
