import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import scoped_session

from core.test_database import TestingSessionLocal, app


@pytest.fixture()
def db():
    Session = scoped_session(TestingSessionLocal)
    session = Session()
    yield session
    session.close()


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
