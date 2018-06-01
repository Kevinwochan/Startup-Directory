#!/bin/sh
#!/bin/sh

$(cd ~/Startupdirectory;
 git reset --hard;
 git pull;
 pipenv install --dev;
pipenv run python manage.py makemigrations;
pipenv run python manage.py migrate;
pipenv run python manage.py shell < downloadStartups.py)
