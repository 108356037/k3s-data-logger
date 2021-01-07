FROM python:3.8-slim

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY ./app/requirements.txt requirements.txt 

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/. .

ENV PYTHONUNBUFFERED=0