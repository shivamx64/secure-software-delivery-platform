import os

from flask import Flask, jsonify

from src.api.health import health_bp
from src.api.metrics import metrics_bp
from src.api.users import users_bp
from src.config import DevelopmentConfig
from src.config import ProductionConfig
from src.config import TestingConfig
from src.database.db import db


CONFIG_MAPPING = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(metrics_bp)
    app.register_blueprint(users_bp)

    @app.route("/", methods=["GET"])
    def index():
        return jsonify(
            {
                "application": "Secure Software Delivery Platform",
                "status": "running",
                "version": "v1",
            }
        )

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    environment = os.getenv("FLASK_ENV", "development").lower()

    config_class = CONFIG_MAPPING.get(
        environment,
        DevelopmentConfig,
    )

    app = create_app(config_class)

    app.run(
        host=os.getenv("FLASK_HOST", "0.0.0.0"),
        port=int(os.getenv("FLASK_PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
    )