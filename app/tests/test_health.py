from src.app import create_app
from src.config import TestConfig


def test_health():
    app = create_app(TestConfig)

    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200