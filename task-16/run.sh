#!/bin/bash
# Task 16: Inter-Container Communication over User-Defined Bridge Network
docker network create super30-net
docker run -d --network super30-net --name server-node nginx:alpine
docker run --rm --network super30-net alpine:latest ping -c 3 server-node
docker stop server-node
docker rm server-node
