from django.urls import path
from .consumers import GameRoom

websocket_urlpatterns = [
    path("ws/play/<room_code>", GameRoom.as_asgi())
]
