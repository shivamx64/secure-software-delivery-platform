from src.app import create_app
from src.database.db import db


def test_health():

    app = create_app()

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()

        client = app.test_client()

        response = client.get("/health")

        assert response.status_code == 200

        db.drop_all()