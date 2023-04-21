import os


"""
###################################################################################################
Do not change ENV variables here! Just create .env and .env.testing (copy .env.example and set your own values)
file in root folder and add these vars there!
###################################################################################################
"""

DB_NAME = os.getenv('DB_NAME')
PGSQL_TEST_DB_NAME = os.getenv('PGSQL_TEST_DB_NAME', 'test_warehouse')

DB_USER_NAME = os.getenv('DB_USER_NAME')
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '031lmefpKDM2KdwdE')

