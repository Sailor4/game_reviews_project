from django.shortcuts import render
from games.models import Game
from reviews.models import Review


def index(request):
    games_count = Game.objects.count()
    reviews_count = Review.objects.count()
    context = {
        'games_count': games_count,
        'reviews_count': reviews_count,
    }

    return render(request, 'common/index.html', context)
