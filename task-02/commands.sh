#!/bin/bash
# Task 2: Create Ubuntu container, install Python, and execute sample Python program
echo "=== Running Ubuntu container, installing Python 3, and running script ==="
docker run --rm --name task2-python ubuntu:latest bash -c "
  apt-get update && apt-get install -y python3 && \
  python3 -c \"print('Docker Ubuntu container running Python successfully!')\"
"
