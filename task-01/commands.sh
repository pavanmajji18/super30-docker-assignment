#!/bin/bash
# Task 1: Pull latest Ubuntu Docker image and execute 5 Linux commands inside container
echo "=== Pulling Ubuntu latest image ==="
docker pull ubuntu:latest

echo "=== Running Ubuntu container and executing 5 Linux commands ==="
docker run --rm --name task1-ubuntu ubuntu:latest bash -c "
  echo '1. Kernel & Architecture:' && uname -a && \
  echo '2. Active User:' && whoami && \
  echo '3. OS Distribution Details:' && cat /etc/os-release && \
  echo '4. Current Working Directory:' && pwd && \
  echo '5. APT Package Manager Refresh:' && apt-get update
"
