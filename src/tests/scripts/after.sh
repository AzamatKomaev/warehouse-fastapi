export APP_ENV=test
alembic -c /var/www/src/alembic.ini downgrade base
export APP_ENV=dev
