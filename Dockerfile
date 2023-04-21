FROM python:3.10-slim

COPY ./src /var/www/src
COPY ./requirements.txt /var/www/src

WORKDIR /var/www/src

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD alembic upgrade head && python main.py
