from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.utils import timezone


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form,'server_time': timezone.now()})
