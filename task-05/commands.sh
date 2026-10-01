#!/bin/bash
# Task 5: Pull Multiple Images & List Local Cache
docker pull python:3.12-slim
docker pull postgres:16-alpine
docker pull nginx:alpine

# Display all local images
docker images
