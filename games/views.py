from django.shortcuts import render, redirect, get_object_or_404
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


def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('game_catalog')

    return render(request, 'games/delete_game.html', {'game': game})


def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_catalog')
    else:
        form = GameForm(instance=game)

    return render(request, 'games/edit_game.html', {'form': form, 'game': game})