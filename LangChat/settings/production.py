from .base import *

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS')

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    'default': env.db()
}

django_heroku.settings(locals())
