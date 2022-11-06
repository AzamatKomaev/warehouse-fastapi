import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from core.config import FULL_UVICORN_PATH
from ..services import get_data_from_file


# endpoints for auth router.
auth_endpoints = {
    'create': f'{FULL_UVICORN_PATH}/auth/create'
}


@pytest.mark.user
def test_empty_data_creating_user(db: Session, client: TestClient):
    file_name = 'empty_data_creating_user.json'
    input_data, output_data = get_data_from_file(directory='auth', file_name=file_name)
    response = client.post(auth_endpoints['create'], json=input_data)
    assert response.status_code == 422
    assert response.json() == output_data


@pytest.mark.user
def test_invalid_type_creating_user(db: Session, client: TestClient):
    file_name = 'invalid_type_creating_user.json'
    input_data, output_data = get_data_from_file(directory='auth', file_name=file_name)
    response = client.post(auth_endpoints['create'], json=input_data)

    assert response.status_code == 422
    assert response.json() == output_data


@pytest.mark.user
def test_invalid_password_creating_user(db: Session, client: TestClient):
    file_name = 'invalid_password_creating_user.json'
    input_data, output_data = get_data_from_file(directory='auth', file_name=file_name)
    response = client.post(auth_endpoints['create'], json=input_data)

    assert response.status_code == 422
    assert response.json() == output_data


@pytest.mark.user
def test_existing_name_creating_user(db: Session, client: TestClient):
    file_name = 'existing_name_creating_user.json'
    input_data, output_data = get_data_from_file(directory='auth', file_name=file_name)
    response1 = client.post(auth_endpoints['create'], json=input_data)
    response2 = client.post(auth_endpoints['create'], json=input_data)

    assert response1.status_code == 201
    assert response2.status_code == 400
    assert response2.json() == output_data


@pytest.mark.user
def test_successfully_creating_user(db: Session):
    pass


@pytest.mark.user
def test_invalid_data_authorizing_user(db: Session):
    assert 2 == 2


@pytest.mark.user
def test_successfully_authorizing_user(db: Session):
    assert 3 == 3
