FROM python:3.9

ENV DJANGO_SETTINGS_MODULE="pur_beurre_project_app.settings.dev-docker"

ADD . /app

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y cron

ADD crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py crontab add
RUN python manage.py crontab show
