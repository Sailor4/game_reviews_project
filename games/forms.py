from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'platform', 'genre', 'release_year', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter game title...'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What is this game about?'}),
        }