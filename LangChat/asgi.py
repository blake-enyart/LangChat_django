"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'LangChat.settings.production'
django.setup()
application = get_default_application()
