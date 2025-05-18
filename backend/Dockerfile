FROM python:3.12-slim

WORKDIR app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
 
RUN python manage.py makemigrations \
    && python manage.py migrate
