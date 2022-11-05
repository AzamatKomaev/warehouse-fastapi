import pytest
import requests
from sqlalchemy.orm import Session
from auth.models import User
from core.config import FULL_UVICORN_PATH
from core.logging import logger
from ..services import get_data_from_file


@pytest.fixture
def set_up_user_tests(db: Session):
    """What to do before and after each user test."""
    yield
    db.query(User).delete()


@pytest.mark.user
def test_auth_empty_data(db: Session):
    data = get_data_from_file(directory='auth', file_name='empty_creating_user_data.json')
    response = requests.post(f'{FULL_UVICORN_PATH}/auth/create', data=data)
    assert response.status_code == 422


@pytest.mark.user
def test_successfully_creating_user(db: Session):
    assert 1 == 1


@pytest.mark.user
def test_invalid_data_authorizing_user(db: Session):
    assert 2 == 2


@pytest.mark.user
def test_successfully_authorizing_user(db: Session):
    assert 3 == 3
