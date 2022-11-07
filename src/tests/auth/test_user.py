import pytest

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from core.config import FULL_UVICORN_PATH
from ..services import get_data_from_file


# endpoints for auth router.
auth_endpoints = {
    'create': f'{FULL_UVICORN_PATH}/auth/create',
    'login': f'{FULL_UVICORN_PATH}/auth/login'
}


@pytest.fixture()
def default_user(db: Session, client: TestClient):
    data = {
        'name': 'admin',
        'type': 'buyer',
        'password': 'admin12345'
    }
    response = client.post(auth_endpoints['create'], json=data)
    assert response.status_code == 201
    yield response.json()


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
def test_successful_creating_user(db: Session, client: TestClient):
    file_name = 'successful_creating_user.json'
    input_data = get_data_from_file(directory='auth', file_name=file_name, return_output=False)[0]
    response = client.post(auth_endpoints['create'], json=input_data)

    assert response.status_code == 201
    assert response.json().get('name') == input_data['name']
    assert response.json().get('type') == input_data['type']
    assert response.json().get('password')


@pytest.mark.user
def test_empty_data_authorizing_user(db: Session, client: TestClient):
    assert 2 == 2


@pytest.mark.user
def test_successfully_authorizing_user(db: Session):
    assert 3 == 3
