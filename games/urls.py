from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_catalog, name='game_catalog'),
    path('add/', views.add_game, name='add_game'),
    path('<int:pk>/delete/', views.delete_game, name='delete_game'),
    path('<int:pk>/edit/', views.edit_game, name='edit_game'),
    path('search/', views.search_games, name='search_games'),
    path('stats/', views.community_stats, name='community_stats')
]
