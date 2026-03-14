from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from games.models import Game

REVIEWER_NAME_MIN_LENGTH = 3
REVIEWER_NAME_MAX_LENGTH = 30
RATING_MIN = 1
RATING_MAX = 10
CONTENT_MIN_LENGTH = 25
CONTENT_MAX_LENGTH = 2500


class Review(models.Model):
    reviewer_name = models.CharField(
        max_length=REVIEWER_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(REVIEWER_NAME_MIN_LENGTH)],
        help_text=f"Minimum {REVIEWER_NAME_MIN_LENGTH} characters."
    )

    content = models.TextField(
        validators=[
            MinLengthValidator(CONTENT_MIN_LENGTH),
            MaxLengthValidator(CONTENT_MAX_LENGTH)
        ],
        help_text=f"Review must be between {CONTENT_MIN_LENGTH} and {CONTENT_MAX_LENGTH} characters."
    )

    rating = models.IntegerField(
        validators=[
            MinValueValidator(RATING_MIN),
            MaxValueValidator(RATING_MAX)
        ]
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.game.title} by {self.reviewer_name}"
