FROM python:3.9

ENV PYTHONUNBUFFERED 1

ADD . /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
