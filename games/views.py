from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm

def game_catalog(request):
    games = Game.objects.all().order_by('title')
    return render(request, 'games/catalog.html', {'games': games})


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_catalog')
    else:
        form = GameForm()

    return render(request, 'games/add_game.html', {'form': form})