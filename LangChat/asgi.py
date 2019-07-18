"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application
import channels.asgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'LangChat.settings'
django.setup()
application = get_default_application()
channel_layer = channels.asgi.get_channel_layer()
