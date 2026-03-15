from django.urls import path
from .views import game_catalog, add_game

urlpatterns = [
    path('', game_catalog, name='game_catalog'),
    path('add/', add_game, name='add_game'),
]
