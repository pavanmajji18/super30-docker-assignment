#!/bin/bash
# Task 7: Build image super30-python-app and run it
docker build -t super30-python-app .
docker run --rm super30-python-app
