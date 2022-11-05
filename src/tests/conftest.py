import pytest
from core.test_database import override_get_db

from . import services


@pytest.fixture(autouse=True, scope='session')
def db():
    """What to do before and after all tests."""
    db = next(override_get_db())
    services.before_tests()
    yield db
    services.after_tests()
