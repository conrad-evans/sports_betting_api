from flask import Flask
from src.routes import sports


def create_app():
    """
    starts instance of a Flask application
    """
    app = Flask(__name__)
    app.register_blueprint(sports)

    return app
