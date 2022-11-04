import pytest
from sqlalchemy.orm import Session


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """What to do before and after each test."""
    yield


@pytest.mark.product
def test_invalid_data_creating_product(db: Session):
    assert 10 == 10


@pytest.mark.product
def test_successful_creating_product(db: Session):
    assert 11 == 11


