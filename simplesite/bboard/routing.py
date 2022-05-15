from django.urls import path
from .consumers import WSCons

ws_urlpatterns = [
    path('ws/some_url/', WSCons.as_asgi())
]