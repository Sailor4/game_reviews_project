from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_catalog, name='game_catalog'),
    path('add/', views.add_game, name='add_game'),
    path('<int:pk>/delete/', views.delete_game, name='delete_game'),
]
