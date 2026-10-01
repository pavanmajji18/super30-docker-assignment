#!/bin/bash
# Task 3: Run Ubuntu container with custom container name
docker run -it --name super30-linux ubuntu:latest bash
# Verify from host:
# docker ps -a --filter "name=super30-linux"
