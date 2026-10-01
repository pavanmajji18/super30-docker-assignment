# Task 2: Install Python Inside Ubuntu Container

## Instructions

1. Start an Ubuntu container interactively:
   ```bash
   docker run -it --name task2-python ubuntu:latest bash
   ```

2. Install Python 3 and run a snippet inside the container:
   ```bash
   apt-get update && apt-get install -y python3
   python3 -c "print('Docker Ubuntu container running Python successfully!')"
   exit
   ```
