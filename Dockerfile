FROM python:3.9-alpine


ADD . /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD exec gunicorn django_in_docker.wsgi:application --bind