# DevOps with Docker, Fall 2026
# offer by The University of Helsinki
# chapter 4/deployment-pipelines
# url: https://courses.mooc.fi/org/uh-cs/courses/devops-with-docker-fall-2026/chapter-4/deployment-pipelines
# Exercise 3.2. Deployment pipeline to a cloud service
# created at Nov 01, 2026 14:09 HKT

import random
import time
import zoneinfo
from datetime import datetime

from fastapi import FastAPI, status

app = FastAPI(title="Random Number API", version="3.0")
START_TIME = time.time()

@app.get("/")
def home():
    """Returns a welcome message when land on home page"""
    return {
        "message": "Welcome to Random Number API v3",
        "usage": "/random",
        "example": "/random?min_val=1&max_val=100"
    }

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Returns the health status, app version, uptime in minutes, and HKT timestamp."""
    hkt_zone = zoneinfo.ZoneInfo("Asia/Hong_Kong")
    current_time_hkt = datetime.now(hkt_zone)
    
    uptime_minutes = (time.time() - START_TIME) / 60

    return {
        "status": "healthy",
        "version": app.version,
        "uptime_minutes": round(uptime_minutes, 2),
        "timestamp": current_time_hkt.isoformat()
    }


@app.get("/random")
def get_random_number(min_val: int = 10000, max_val: int = 99999):
  """Returns a random integer between min_val and max_val (inclusive)."""
  if min_val > max_val:
    return {"error": "min_val cannot be greater than max_val"}

  return {
      "min": min_val,
      "max": max_val,
      "random_number": random.randint(min_val, max_val),
  }