from flask import Flask
from flask import jsonify

from src.api.health import health_bp
from src.api.metrics import metrics_bp
from src.api.users import users_bp
from src.config import DevelopmentConfig
from src.config import TestingConfig
from src.database.db import db


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

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


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )