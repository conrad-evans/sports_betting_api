from flask import Flask
from src.routes import sports
from src.db import DataBase
from src.sqlite_db import SqliteDataBase

db_name = "sports_betting.db"


def create_app():
    """
    starts instance of a Flask application
    """
    app = Flask(__name__)
    app.register_blueprint(sports)

    global db_name
    sqlite_db = SqliteDataBase.getInstance(db_name)
    db = DataBase.getInstance(sqlite_db)

    return app
