# 1. Defines the base operating system and runtime layer
FROM python:3.12-slim

# 2. Sets the working directory inside the container for all subsequent commands
WORKDIR /app

# 3. Copies dependencies separately to maximize Docker layer caching
COPY requirements.txt .

# 4. Executes commands at build time to produce new filesystem layers
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copies the remaining application code into the WORKDIR
COPY . .

# 6. Documentation directive indicating which port the container listens on at runtime
EXPOSE 8000

# 7. Specifies the default command executed when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
