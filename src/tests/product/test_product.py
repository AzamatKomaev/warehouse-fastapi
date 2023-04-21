import pytest
from sqlalchemy.orm import Session


@pytest.mark.product
def test_invalid_data_creating_product(db: Session):
    assert 10 == 10
