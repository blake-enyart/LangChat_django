from .base import *

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
