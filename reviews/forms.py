from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'game', 'rating', 'content']

        widgets = {
            'reviewer_name': forms.TextInput(attrs={'placeholder': 'Enter your name...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Please tell us here, what do you think of the game', 'rows': 4}),
        }