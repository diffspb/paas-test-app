from fastapi.testclient import TestClient

from app.main import APP_VERSION, SERVICE_NAME, app


client = TestClient(app)


def test_root_returns_placeholder_payload():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == SERVICE_NAME
    assert response.json()["message"] == "PaaS test application is running"
    assert response.json()["version"] == APP_VERSION


def test_health_contract():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": APP_VERSION,
    }


def test_version_endpoint():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["service"] == SERVICE_NAME
    assert response.json()["version"] == APP_VERSION
