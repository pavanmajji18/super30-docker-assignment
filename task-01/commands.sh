#!/bin/bash
# Task 1: Pull the latest Ubuntu Docker image and run it interactively
docker pull ubuntu:latest

# Run interactively:
# docker run -it --name task1-ubuntu ubuntu:latest bash

# Commands executed inside the container:
# 1. uname -a                     # Check kernel & system architecture
# 2. whoami                       # View active user (root)
# 3. cat /etc/os-release          # View OS distribution details
# 4. pwd                          # Print working directory
# 5. apt-get update               # Refresh package manager indexes
# exit
