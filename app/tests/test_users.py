from src.app import create_app
from src.config import TestConfig


def test_root():
    app = create_app(TestConfig)

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200