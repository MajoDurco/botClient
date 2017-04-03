FROM python:3.5-alpine

WORKDIR /usr/src

COPY client.py constants.py wait-for-it.sh ./

RUN apk update; apk add bash

CMD python3 ./client.py
