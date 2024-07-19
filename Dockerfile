FROM python:3.12-slim

WORKDIR /electronics_shop

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
