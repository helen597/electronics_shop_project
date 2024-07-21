FROM python:3.12-slim

WORKDIR /electronics_shop_project

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
