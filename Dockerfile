FROM python:3.9

ENV DJANGO_SETTINGS_MODULE="pur_beurre_project_app.settings.production"

ADD . /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
