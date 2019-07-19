from .base import *

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

import dj_database_url
DATABASES = {
'default': dj_database_url.config(default=env('DATABASE_URL'), conn_max_age=600, ssl_require=True)
}
