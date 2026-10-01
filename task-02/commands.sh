#!/bin/bash
# Task 2: Create an Ubuntu container, install Python inside it, and execute a Python program
echo "=== Launching Ubuntu container, installing Python 3, and executing Python snippet ==="
docker run --rm --name task2-python ubuntu:latest bash -c "
  apt-get update && apt-get install -y python3 && \
  python3 -c \"print('Docker Ubuntu container running Python successfully!')\"
"
