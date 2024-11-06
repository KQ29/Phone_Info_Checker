# Use the official Python 3.13.0 image as the base image
FROM python:3.13.0-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the main Python file
CMD ["python", "phone_number_checker.py"]
