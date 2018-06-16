#!/bin/sh

$(cd ~/startupdirectory;
 git reset --hard;
 git pull;
 pipenv install --dev;
 rm -f *.sqlite3;
pipenv run python manage.py migrate --run-syncdb;
pipenv run python manage.py makemigrations;
pipenv run python manage.py migrate;
pipenv run python manage.py shell < downloadStartups.py;
chmod 664 ~/startupdirectory/*.sqlite3;
sudo chown :www-data ~/startupdirectory;
sudo chown :www-data ~/startupdirectory/*.sqlite3;
) > /home/ubuntu/update.log
