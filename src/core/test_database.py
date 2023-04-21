from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from .database import get_db, Base
from . import config


SQLALCHEMY_TEST_DATABASE_URL = 'postgresql+pg8000://{0}:{1}@{2}:{3}/{4}'.format(
    config.PGSQL_USER_NAME,
    config.PGSQL_PASSWORD,
    config.PGSQL_HOST,
    5432,
    config.PGSQL_TEST_DB_NAME
)

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
