from django.shortcuts import render
from .models import Game

def game_catalog(request):
    games = Game.objects.all().order_by('title')
    return render(request, 'games/catalog.html', {'games': games})
