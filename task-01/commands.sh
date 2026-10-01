#!/bin/bash
# Task 1: Pull the latest Ubuntu Docker image and run it interactively
echo "=== Pulling Ubuntu latest image ==="
docker pull ubuntu:latest

echo "=== Executing 5 Linux commands inside Ubuntu container ==="
docker run --rm ubuntu:latest bash -c "
  echo '1. Kernel & Architecture:' && uname -a && \
  echo '2. Active User:' && whoami && \
  echo '3. OS Distribution Details:' && cat /etc/os-release && \
  echo '4. Current Working Directory:' && pwd && \
  echo '5. APT Package Manager Refresh:' && apt-get update
"

echo "=== Launching interactive Ubuntu container session ==="
docker run -it --name task1-ubuntu ubuntu:latest bash
