import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import scoped_session

from core.test_database import TestingSessionLocal, app, Base, engine


@pytest.fixture()
def db():
    Base.metadata.create_all(bind=engine)
    session = scoped_session(TestingSessionLocal)()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
