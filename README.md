# Textbook Ventures Startup Directory
## App Features ##
Directory
    displays a list of companies in a tabular format
    displays a company's profile page with additional information

Registration

## Useful Utilities

CSV to DB saver

Save file "startup.csv" in project folder 
Run by passing the program into Django's Shell

    pipenv run python manage.py shell < csvTosql.py 

Downlad latest startups from google sheets

    pipenv run python manage.py shell < downloadStartups.py 

## Dependencies

- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Pipenv](https://docs.pipenv.org) To manage dependences and virtualenvs.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for superusers.
- [Argon2](https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#using-argon2-with-django) to hash the passwords
- [Pillow] (https://github.com/python-pillow) to handle images
- [Sheets API]
- [Oauth2] 

## Local Host Setup

1. Install Python3
2. Install Pip3 (Python3 package manager)
3. Install Pipenv 
4. Run install script (install.sh)
5. Run update script (update.sh)


Make sure you have [pipenv installed](https://docs.pipenv.org/install.html). Then install Django 2.0 in your virtualenv:

    pip install django==2.0

   
## How to run on local host

Once everything it's setup, make sure to update your files with the latest dataset and code using update.sh.

Run the development server: [http://localhost:8000/](http://localhost:8000/)

    pipenv run python manage.py runserver

The Settings are divided by environments: production.py, development.py and testing.py. By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE="my_project.settings.production"

or you can use the `settings` param with runserver:

    pipenv run python manage.py runserver --settings=my_project.settings.production

If you need to add some settings that are specific for your machine, rename the file `local_example.py` to `local_settings.py`. This file it's in .gitignore so the changes won't be tracked.
