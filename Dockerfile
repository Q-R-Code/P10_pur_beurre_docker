FROM python:3.9

ENV DJANGO_SETTINGS_MODULE="pur_beurre_project_app.settings.dev-docker"

ADD . /app

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y cron


RUN pip install --no-cache-dir -r requirements.txt

