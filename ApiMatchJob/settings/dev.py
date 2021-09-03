from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'MatchJob',
        'USER': 'MatchJob',
        'PASSWORD': 'QueHayDeNuevoViejo',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'client_encoding': 'UTF8',
    }
}

