import os

from dotenv import load_dotenv
from flask import Flask

def create_app(test_config=None):
    """Create and configure a Flask application instance."""
    load_dotenv()

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    app.config.from_mapping(
        SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret-key"),
        MAX_CONTENT_LENGTH = 8*1024*1024,
    )

    if test_config:
        app.config.update(test_config)

    from app.routes import main

    app.register_blueprint(main)
    return app
