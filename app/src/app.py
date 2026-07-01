from flask import Flask

from config import Config


def create_app() -> Flask:

    app = Flask(__name__)

    app.config.from_object(Config)

    @app.get("/")
    def index():
        return {
            "application": Config.APP_NAME,
            "version": Config.API_VERSION,
            "status": "running",
        }

    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
    )