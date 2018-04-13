import os
from sys import path
from .base import *  # noqa

# PATHS
# Path containing the django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path.append(BASE_DIR)

# Path of the top level directory.
# This directory contains the django project, apps, libs, etc...
PROJECT_ROOT = os.path.dirname(BASE_DIR)

DEBUG = False

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

# ALLOWED HOSTS
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.textbook.ventures/*',
                 '13.211.154.14',
                 'ec2-13-211-154-14.ap-southeast-2.compute.amazonaws.com',
                 '*',
]
# DATABASE SETTINGS
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT,'development.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache"
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# IMPORTANT!:
# You must keep this secret, you can store it in an
# environment variable and set it with:
# export SECRET_KEY="phil-dunphy98!-bananas12"
# https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/#secret-key
SECRET_KEY = 'rocketbook'

# WSGI SETTINGS
# https://docs.djangoproject.com/en/1.10/ref/settings/#wsgi-application
WSGI_APPLICATION = 'startupdirectory.wsgi.application'

# NOTIFICATIONS
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/1.10/ref/settings/#admins
ADMINS = (
         ('Kevin Chan','kevinwochan@gmail.com'),
)
MANAGERS = ADMINS

# DJANGO-COMPRESSOR SETTINGS
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
)

try:
    from local_settings import * # noqa
except ImportError:
    pass
