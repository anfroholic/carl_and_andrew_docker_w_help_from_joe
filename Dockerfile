# syntax=docker/dockerfile:1
FROM python:3.14.0
ENV PYTHONDONTWRITEBYTECODE=0
ENV PYTHONUNBUFFERED=0
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/