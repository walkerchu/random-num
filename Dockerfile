# DevOps with Docker, Fall 2026
# offer by The University of Helsinki
# chapter 4/deployment-pipelines
# url: https://courses.mooc.fi/org/uh-cs/courses/devops-with-docker-fall-2026/chapter-4/deployment-pipelines
# Exercise 3.2. Deployment pipeline to a cloud service
# created at Nov 01, 2026 14:09 HKT

# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI server using Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]