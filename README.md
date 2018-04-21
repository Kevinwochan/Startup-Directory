 _____              _    _                    _      
|_   _|            | |  | |                  | |     
  | |    ___ __  __| |_ | |__    ___    ___  | | __  
  | |   / _ \\ \/ /| __|| '_ \  / _ \  / _ \ | |/ /  
  | |  |  __/ >  < | |_ | |_) || (_) || (_) ||   <   
  \_/   \___|/_/\_\ \__||_.__/  \___/  \___/ |_|\_\  
                                                     
                                                     
 _   _               _                       _       
| | | |             | |                     ( )      
| | | |  ___  _ __  | |_  _   _  _ __   ___ |/  ___  
| | | | / _ \| '_ \ | __|| | | || '__| / _ \   / __| 
\ \_/ /|  __/| | | || |_ | |_| || |   |  __/   \__ \ 
 \___/  \___||_| |_| \__| \__,_||_|    \___|   |___/ 
                                                     
                                                     
 _____  _                 _                          
/  ___|| |               | |                         
\ `--. | |_   __ _  _ __ | |_  _   _  _ __           
 `--. \| __| / _` || '__|| __|| | | || '_ \          
/\__/ /| |_ | (_| || |   | |_ | |_| || |_) |         
\____/  \__| \__,_||_|    \__| \__,_|| .__/          
                                     | |             
                                     |_|             
______  _                    _                       
|  _  \(_)                  | |                      
| | | | _  _ __   ___   ___ | |_   ___   _ __  _   _ 
| | | || || '__| / _ \ / __|| __| / _ \ | '__|| | | |
| |/ / | || |   |  __/| (__ | |_ | (_) || |   | |_| |
|___/  |_||_|    \___| \___| \__| \___/ |_|    \__, |
                                                __/ |
                                               |___/ 

##################
## App Features ##
##################
Directory
    displays a list of companies in a tabular format
    displays a company's profile page with additional information
    
Registration

####################
# Useful Utilities #
####################

CSV to DB saver

Save file "startup.csv" in project folder 
Run by passing the program into Django's Shell

    pipenv run python manage.py shell < csvTosql.py 

##################
## Dependencies ##
##################

- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Pipenv](https://docs.pipenv.org) To manage dependences and virtualenvs.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for superusers.
- [Argon2](https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#using-argon2-with-django) to hash the passwords
- [Pillow] (https://github.com/python-pillow) to handle images

######################
## Local Host Setup ##
######################

1. Install Python3
2. Install Pip3 (Python3 package manager)
3. Install Pipenv 
4. Install Pip Dependencies

Make sure you have [pipenv installed](https://docs.pipenv.org/install.html). Then install Django 2.0 in your virtualenv:

    pip install django==2.0

To create a new Django project (make sure to change `project_name`)

    django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt project_name

cd to your project and install the development dependences

    pipenv install --dev

If you need a database, edit the settings and create one with
   
    pipenv run python manage.py migrate

    
##############################
## How to run on local host ##
##############################


Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    pipenv run python manage.py runserver

The Settings are divided by environments: production.py, development.py and testing.py. By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE="my_project.settings.production"

or you can use the `settings` param with runserver:

    pipenv run python manage.py runserver --settings=my_project.settings.production

If you need to add some settings that are specific for your machine, rename the file `local_example.py` to `local_settings.py`. This file it's in .gitignore so the changes won't be tracked.
