from practice.consumers import MySyncConsumer
from django.urls import path
websocket_urlpatterns=[
    path('sc/<str:groupkaname>/',MySyncConsumer.as_asgi())
]