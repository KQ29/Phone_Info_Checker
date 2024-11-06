# Use the official Python 3.13.0 slim image as the base image
FROM python:3.13.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt separately to leverage caching
COPY requirements.txt .

# Install dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Add a non-root user for security
RUN adduser --disabled-password appuser
USER appuser

# Set environment variables
ENV APP_ENV=production
ENV APP_DEBUG=False

# Set the entry point for the container
ENTRYPOINT ["python", "phone_number_checker.py"]
