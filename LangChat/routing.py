from .token_auth import TokenAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
import chat_app.routing
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': TokenAuthMiddleware(
        URLRouter(
            chat_app.routing.websocket_urlpatterns
        )
    ),
})
