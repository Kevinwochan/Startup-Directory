#!/bin/sh

$(cd ~/startupdirectory; git pull; pipenv run python manage.py migrate;)

