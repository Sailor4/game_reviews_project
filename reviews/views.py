from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from django.utils import timezone
from .models import Review


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form,'server_time': timezone.now()})


def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        review.delete()
        return redirect('review_list')

    return render(request, 'reviews/delete_review.html', {'review': review})


def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

