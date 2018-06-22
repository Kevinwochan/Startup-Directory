#!/bin/sh
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
echo "=== log entry $timestamp ==="
cd ~/startupdirectory;
git reset --hard;
git pull;
pipenv run python manage.py migrate --run-syncdb;
pipenv run python manage.py makemigrations;
pipenv run python manage.py migrate;
pipenv run python manage.py shell < downloadStartups.py;
sudo chmod +rw ~/startupdirectory/*.sqlite3;
sudo chown :www-data ~/startupdirectory;
sudo chown :www-data ~/startupdirectory/*.sqlite3;
echo "==========================="
