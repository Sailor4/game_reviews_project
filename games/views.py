from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm
from django.db.models import Q, Count, Avg
from reviews.models import Review

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

def search_games(request):
    query = request.GET.get('q')
    results = Game.objects.all()

    if query:
        results = results.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'games/search_results.html', {
        'results': results,
        'query': query
    })

def community_stats(request):
    total_games = Game.objects.count()
    total_reviews = Review.objects.count()

    top_reviewers = Review.objects.values('reviewer_name').annotate(
        review_count=Count('reviewer_name')
    ).order_by('-review_count')[:5]

    top_pc = Game.objects.filter(platform='PC').annotate(
        avg_rating=Avg('reviews__rating')
    ).filter(avg_rating__isnull=False).order_by('-avg_rating').first()

    top_console = Game.objects.filter(platform='Console').annotate(
        avg_rating=Avg('reviews__rating')
    ).filter(avg_rating__isnull=False).order_by('-avg_rating').first()

    return render(request, 'games/community_stats.html', {
        'total_games': total_games,
        'total_reviews': total_reviews,
        'top_reviewers': top_reviewers,
        'top_pc': top_pc,
        'top_console': top_console,
    })

