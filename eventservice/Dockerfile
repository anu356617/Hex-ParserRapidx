# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /eventservice

# Install git and other necessary dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at 
COPY . .

ENV ENVIRONMENT=development

# Copy .env file for development
COPY .env .

# Run app.py when the container launches
CMD ["python", "app.py"]
