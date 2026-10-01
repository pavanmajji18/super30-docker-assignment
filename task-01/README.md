# Task 1: Pull and Run Interactive Ubuntu

## Instructions

1. Pull the latest Ubuntu image:
   ```bash
   docker pull ubuntu:latest
   ```

2. Run the container interactively:
   ```bash
   docker run -it --name task1-ubuntu ubuntu:latest bash
   ```

3. Inside the container shell, execute five Linux commands:
   ```bash
   uname -a            # 1. Check kernel & architecture
   whoami              # 2. View current user (root)
   cat /etc/os-release # 3. View OS details
   pwd                 # 4. View working directory
   apt-get update      # 5. Update package manager
   exit                # Exit container
   ```
