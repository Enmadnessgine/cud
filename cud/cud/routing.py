from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from cud.cud.consumers import PlayerCoordinatesConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        path("ws/player_coordinates/", PlayerCoordinatesConsumer.as_asgi()),
    ),
})