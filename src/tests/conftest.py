import pytest
from core.test_database import override_get_db

from . import services


@pytest.fixture(scope='session')
def db():
    """What to do before and after all tests."""
    db = next(override_get_db())
    services.before_tests(db)
    yield db
    services.after_tests(db)
