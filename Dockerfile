FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

WORKDIR /mysite
COPY ./mysite /mysite

RUN mkdir -p /vol/web/static
RUN python manage.py collectstatic --no-input
RUN adduser -D myuser
RUN chown -R myuser:myuser /vol/
RUN chmod -R 755 /vol/web
USER myuser