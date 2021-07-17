# pull official base image
FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY
ARG DJANGO_CORS_ORIGIN_WHITELIST

# set environment variables, variables have real value in core/settings.py
# 장고 whitelist, allowed host, cors 관련 설정 (변수 형태로 들어감), core/settings.py와 매핑
ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DJANGO_CORS_ORIGIN_WHITELIST $DJANGO_CORS_ORIGIN_WHITELIST

WORKDIR /mysite
COPY requirements.txt /mysite/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /mysite/