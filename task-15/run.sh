#!/bin/bash
# Task 15: Create volume, store data, remove container, read data from new container
docker volume create super30-data
docker run --rm -v super30-data:/data ubuntu:latest bash -c "echo 'Persisted Docker Data' > /data/message.txt"
docker run --rm -v super30-data:/data ubuntu:latest cat /data/message.txt
