from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_review, name='add_review'),
    path('', views.review_list, name='review_list'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
    path('edit/<int:pk>/', views.edit_review, name='edit_review')
]
