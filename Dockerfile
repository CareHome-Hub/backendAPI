FROM python:3.6-alpine

RUN apk update && apk add git

RUN mkdir /app
WORKDIR /app

RUN pip install pip --upgrade
RUN apk add gcc
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="spanarchian <spanarchian@gmail.com>" \
      version="0.1"

CMD flask run --host=0.0.0.0 --port=5000