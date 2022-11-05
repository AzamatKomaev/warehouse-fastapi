import os


"""
###################################################################################################
Do not change ENV variables here! Just create .env and .env.testing (copy .env.example and set your own values)
file in root folder and add these vars there!
###################################################################################################
"""

APP_ENV = os.getenv('APP_ENV', 'dev')

PGSQL_DEV_DB_NAME = os.getenv('PGSQL_DEV_DB_NAME', 'dev_warehouse')
PGSQL_TEST_DB_NAME = os.getenv('PGSQL_TEST_DB_NAME', 'test_warehouse')

PGSQL_USER_NAME = os.getenv('PGSQL_USER_NAME', 'azamat')
PGSQL_PASSWORD = os.getenv('PGSQL_PASSWORD', 'dev12345')
PGSQL_HOST = os.getenv('PGSQL_HOST', 'db')
PGSQL_PORT = os.getenv('PGSQL_PORT', 5432)

UVICORN_PORT = os.getenv('UVICORN_PORT', 8000)
UVICORN_HOST = os.getenv('UVICORN_HOST', '127.0.0.1')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '031lmefpKDM2KdwdE')


FULL_UVICORN_PATH = f'http://{UVICORN_HOST}:8000'
