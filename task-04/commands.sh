#!/bin/bash
# Task 4: Detached Mode, Lifecycle & Removal
docker run -d --name super30-detached ubuntu:latest sleep 3600
docker ps --filter "name=super30-detached"
docker stop super30-detached
docker restart super30-detached
docker stop super30-detached
docker rm super30-detached
