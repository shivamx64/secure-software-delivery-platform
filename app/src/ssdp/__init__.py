from flask import Flask
from .config import get_config
from .routes.health import health_bp
from .routes.users import users_bp


def create_app():
    app = Flask(__name__)

    # load config (env-based later)
    app.config.from_object(get_config())

    # register blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)

    return app