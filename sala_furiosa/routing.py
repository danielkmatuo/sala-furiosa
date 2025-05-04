from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from app_sala_furiosa import routing as app_routing

websocket_application = AuthMiddlewareStack(
    URLRouter(
        app_routing.websocket_urlpatterns
    )
)
