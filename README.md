# Random Number API v3

This project was created for [Exercise 3.2: Deployment Pipeline to a Cloud Service in the DevOps with Docker (Fall 2026) course](https://courses.mooc.fi/org/uh-cs/courses/devops-with-docker-fall-2026/chapter-4/deployment-pipelines) offered by the University of Helsinki.

The application is built with FastAPI and returns random numbers within a user-defined range. It also provides a health check endpoint to verify that the service is running.

## Important Url

- GitHub: https://github.com/walkerchu/random-num.git

- Docker Hub: https://hub.docker.com/r/walkerchu/random-num-cloud

- Live Service at Render: https://random-num-cloud.onrender.com

## Deployment Pipeline

1. Reused the Random Number API developed in previous exercises.
2. Created a Dockerfile based on the python:3.11-slim image.
3. Created a docker-compose.yaml file to provide a Docker-based development environment.
4. Enhanced the API and added automated tests using Pytest and FastAPI TestClient.
5. Created a public Docker Hub repository: `walkerchu/random-num-cloud`.
6. Created a public GitHub repository: `walkerchu/random-num`.
7. Created a Render web service: `random-num-cloud`.
8. Pushed the source code to GitHub.
9. GitHub Actions automatically runs the pipeline:
    - Run Ruff code checks
    - Run Pytest test cases
    - Build a Docker image
    - Push the image to Docker Hub
    - Deploy the latest image to Render using a deploy hook
10. Confirmed that the application is publicly available through the Render URL.

## Features

- Generate random numbers within a custom range
- Health check endpoint
- Docker container support
- Automated testing with Pytest and FastAPI TestClient
- Automated CI/CD with GitHub Actions
- Cloud deployment on Render

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | API welcome message and basic usage instructions. |
| `GET` | `/health` | Health status check, app version, system uptime, and current HKT time. |
| `GET` | `/random` | Returns a random integer. Supports query parameters `min_val` and `max_val`. |

### Endpoint Details

#### 1. Root Endpoint
- **URL**: `GET /`
- **Response Example**:
  ```json
  {
    "message": "Welcome to Random Number API v3",
    "usage": "/random",
    "example": "/random?min_val=1&max_val=100"
  }
  ```

#### 2. Health Check
- **URL**: `GET /health`
- **Status Code**: `200 OK`
- **Response Example**:
  ```json
  {
    "status": "healthy",
    "version": "3.0",
    "uptime_minutes": 8.15,
    "timestamp": "2026-11-07T09:06:33.587560+08:00"
  }
  ```

#### 3. Random Number Generator
- **URL**: `GET /random`
- **Query Parameters**:
  - `min_val` *(int, default: 10000)*: Minimum boundary (inclusive).
  - `max_val` *(int, default: 99999)*: Maximum boundary (inclusive).
- **Request Example**:
  ```bash
  GET /random?min_val=1&max_val=100
  ```
- **Response Example**:
  ```json
  {
    "min": 1,
    "max": 100,
    "random_number": 42
  }
  ```


## Project Requirements

### `requirements.txt`
```text
fastapi>=0.100.0
uvicorn>=0.22.0
pytest>=8.0.0
httpx>=0.25.0
ruff>=0.13.0
```
> **Note**: Requires **Python 3.9+** for standard library support of `zoneinfo`.



## Local Development

### Build the development environment
```bash
docker compose build
```

### Start a development container
```Shell
docker compose run --rm dev bash
```

### Inside the container, run the tests
```Shell
pytest -v
```

### Start the API
```Shell
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Open
```Plain Test
http://localhost:8000
```

---
Date : Nov 7 2026