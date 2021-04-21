from flask import Flask


def create_app():
    """
    starts instance of a Flask application
    """
    app = Flask(__name__)

    return app
