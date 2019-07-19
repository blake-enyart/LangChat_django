from .base import *

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')

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

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

django_heroku.settings(locals())
