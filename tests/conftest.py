import pytest
from src import create_app


@pytest.fixture
def client():
    """
    app fixture for configuring the application for testing
    """
    client = create_app().test_client()

    yield client


# this fixture is not necessary for running tests in this repo
# Although I will keep it here for future references
# @pytest.fixture
# def db():
#     """
#     fixure to setup in memory database for testing
#     """
#     conn = sqlite3.connect(':memory:')
#     cursor = conn.cursor()
#     cursor.execute(SCHEMA)

#     yield conn
