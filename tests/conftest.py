import pytest
from src import create_app


@pytest.fixture
def client():
    """
    app fixture for configuring the application for testing
    """
    client = create_app().test_client()

    yield client
