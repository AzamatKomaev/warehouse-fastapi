#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$PGSQL_USER_NAME" --dbname "$PGSQL_DEV_DB_NAME" <<-EOSQL
    CREATE DATABASE "$PGSQL_TEST_DB_NAME";
EOSQL
