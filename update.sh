#!/bin/sh
#!/bin/sh

$(cd ~/Startupdirectory;
 git reset --hard;
 git pull;
 pipenv install --dev;
 rm -f *.sqlite3;
pipenv run python manage.py migrate --sync-db;
pipenv run python manage.py makemigrations;
pipenv run python manage.py migrate;
pipenv run python manage.py shell < downloadStartups.py)
