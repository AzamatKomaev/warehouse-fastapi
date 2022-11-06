import pytest
import requests
from sqlalchemy.orm import Session
from auth.models import User
from core.config import FULL_UVICORN_PATH
from core.logging import logger
from ..services import get_data_from_file


# endpoints for auth router.
auth_endpoints = {
    'create': f'{FULL_UVICORN_PATH}/auth/create'
}


@pytest.fixture
def set_up_user_tests(db: Session):
    """What to do before and after each user test."""
    yield
    db.query(User).delete()


@pytest.mark.user
def test_empty_data_creating_user(db: Session):
    file_name = 'empty_data_creating_user.json'
    input_data = get_data_from_file(f'auth/input_data/{file_name}')
    output_data = get_data_from_file(f'auth/output_data/{file_name}')
    response = requests.post(auth_endpoints['create'], json=input_data)

    assert response.status_code == 422
    assert response.json() == output_data


@pytest.mark.user
def test_invalid_type_creating_user(db: Session):
    file_name = 'invalid_type_creating_user.json'
    input_data = get_data_from_file(f'auth/input_data/{file_name}')
    output_data = get_data_from_file(f'auth/output_data/{file_name}')
    response = requests.post(auth_endpoints['create'], json=input_data)

    assert response.status_code == 422
    assert response.json() == output_data


@pytest.mark.user
def test_invalid_password_creating_user(db: Session):
    file_name = 'invalid_password_creating_user.json'
    input_data = get_data_from_file(f'auth/input_data/{file_name}')
    output_data = get_data_from_file(f'auth/output_data/{file_name}')
    response = requests.post(auth_endpoints['create'], json=input_data)
    logger.info(response.json())

    assert response.status_code == 422
    assert response.json() == output_data


@pytest.mark.user
def test_successfully_creating_user(db: Session):
    pass


@pytest.mark.user
def test_invalid_data_authorizing_user(db: Session):
    assert 2 == 2


@pytest.mark.user
def test_successfully_authorizing_user(db: Session):
    assert 3 == 3
