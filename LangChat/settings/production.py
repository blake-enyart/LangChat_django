from .base import *

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

DATABASE_URL = env('DATABASE_URL')

DATABASES = {}

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
