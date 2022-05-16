from django.urls import path
from .consumers import WSCons,WSConsUSD

ws_urlpatterns = [
    path('ws/some_url/', WSCons.as_asgi()),
    path('ws/some_urlUSD/', WSConsUSD.as_asgi())
]