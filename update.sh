#!/bin/sh
#!/bin/sh

$(cd ~/Startupdirectory;
 git pull;
 pipenv install --dev;
pipenv run python manage.py makemigrations;
pipenv run python manage.py migrate;
pipenv run python maNage.py shell < downloadStartups.py)
