#!/bin/bash

mkdir -p  /var/data;

if [[ -z "$1" ]]; then
    echo "run server";
    python manage.py migrate;
    python manage.py collectstatic --noinput;
    gunicorn -w 5 -b 0.0.0.0:8000 tisecret.wsgi;
else
    echo "$@"
    exec "$@"
fi
