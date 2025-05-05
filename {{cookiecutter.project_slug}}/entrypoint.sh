#!/bin/bash

python manage.py collectstatic --noinput
cp -r /static_source/. /static/
python manage.py migrate
make load_data
make create_admin
gunicorn {{cookiecutter.project_slug}}.wsgi -b 0.0.0.0:8080