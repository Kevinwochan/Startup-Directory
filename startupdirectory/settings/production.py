import os
from .base import *  # noqa

DEBUG = False
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

# DATABASE SETTINGS
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'development.sqlite3',
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
         ('Your Name', 'your_email@example.com'),
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
