import os
import pytest
from sqlalchemy.orm import Session
from core.test_database import override_get_db
from auth.models import User
from auth.hashing import get_password_hash


def before_tests(db: Session) -> None:
    if os.system('sh ./scripts/before.sh') != 0:
        raise ValueError('Could not run before.sh script.')

    new_user = User(name='test_user', type='buyer', password=get_password_hash('test123'))
    db.add(new_user)
    db.commit()


def after_tests(db: Session) -> None:
    db.query(User).filter(User.name == 'test_user').delete()
    db.commit()

    if os.system('sh ./scripts/after.sh') != 0:
        raise ValueError('Could not run after.sh script.')


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    """What to do before and after main tests."""
    db = next(override_get_db())
    before_tests(db)
    yield
    after_tests(db)
