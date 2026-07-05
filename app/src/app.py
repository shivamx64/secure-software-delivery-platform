"""
Application entry point.
"""

from flask import Flask
from flask import jsonify

from api.health import health_bp
from api.metrics import metrics_bp
from api.users import users_bp
from config import Config
from database.db import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

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