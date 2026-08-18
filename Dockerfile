# Start with a lightweight Linux server that already has Python 3.10
FROM python:3.10-slim

# Copy everything in our current folder into the container's /app folder
COPY . /app

# Change our working directory to /app
WORKDIR /app

# Run the test
CMD ["python3", "test.py"]
