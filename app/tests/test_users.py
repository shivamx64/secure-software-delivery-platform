from src.app import create_app

def test_root():
    app = create_app(testing=True)

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    assert response.get_json() == {
        "application": "Secure Software Delivery Platform",
        "status": "running",
        "version": "v1",
    }