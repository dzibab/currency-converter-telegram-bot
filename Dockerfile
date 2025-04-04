# Use the official Python image as the base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Set the PYTHONPATH environment variable to the /app directory
ENV PYTHONPATH=/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir uv
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Run the bot when the container starts
CMD ["python", "app/main.py"]