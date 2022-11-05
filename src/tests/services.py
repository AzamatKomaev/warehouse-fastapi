import os
import json
from sqlalchemy.orm import Session
from core.logging import logger

from auth.models import User
from auth.hashing import get_password_hash


def before_tests(db: Session) -> None:
    logger.info('Hello it is before_tests script')
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


def get_data_from_file(directory: str, file_name: str) -> dict:
    with open(f'{directory}/data/{file_name}', 'r') as f:
        json_data = json.load(f)
    return json_data
