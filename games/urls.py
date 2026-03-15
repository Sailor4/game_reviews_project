from django.urls import path
from .views import game_catalog

urlpatterns = [
    path('', game_catalog, name='game_catalog'),
]