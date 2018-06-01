#!/bin/sh

$(cd ~/startupdirectory; git pull; pipenv install --dev;pipenv run python manage.py migrate;)
