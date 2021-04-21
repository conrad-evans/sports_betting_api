import sqlite3
import pytest
from src import create_app
from src.schema import SCHEMA


@pytest.fixture
def client():
    """
    app fixture for configuring the application for testing
    """
    client = create_app().test_client()

    yield client


@pytest.fixture
def db():
    """
    fixure to setup in memory database for testing
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute(SCHEMA)

    yield conn
