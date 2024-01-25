import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from cud.consumers import PlayerCoordinatesConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cud.settings')

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        [
            path("ws/player_coordinates/", PlayerCoordinatesConsumer.as_asgi()),
        ],  
    ),
    "http": get_asgi_application(),
})
