from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import config


SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://{db_user_name}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
    db_user_name=config.DB_USER_NAME,
    db_password=config.DB_PASSWORD,
    db_host=config.DB_HOST,
    db_port=config.DB_PORT,
    db_name=config.DB_NAME
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

