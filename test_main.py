# DevOps with Docker, Fall 2026
# offer by The University of Helsinki
# chapter 4/deployment-pipelines
# url: https://courses.mooc.fi/org/uh-cs/courses/devops-with-docker-fall-2026/chapter-4/deployment-pipelines
# Exercise 3.2. Deployment pipeline to a cloud service
# created at Nov 01, 2026 16:33 HKT

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_random():
    response = client.get("/random")

    assert response.status_code == 200

    data = response.json()

    assert "min" in data
    assert "max" in data
    assert "random_number" in data

    assert data["min"] == 10000
    assert data["max"] == 99999

    assert data["min"] <= data["random_number"] <= data["max"]


def test_range():
    response = client.get("/random?min_val=1&max_val=10")

    assert response.status_code == 200

    number = response.json()["random_number"]
    assert 1 <= number <= 10


def test_invalid_parameter():
    response = client.get("/random?min_val=abc")

    assert response.status_code == 422
