from .base import *

ALLOWED_HOST = env('DJANGO_ALLOWED_HOSTS')

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(ssl_require=True)
}
