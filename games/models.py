from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

TITLE_MAX_LENGTH = 30
GENRE_MAX_LENGTH = 20
RATING_MIN_VALUE = 1
RATING_MAX_VALUE = 10.0


class Game(models.Model):
    PLATFORM_CHOICES = (
        ("Console", "Console"),
        ("PC", "PC"),
    )

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        unique=True
    )

    platform = models.CharField(
        max_length=10,
        choices=PLATFORM_CHOICES
    )

    rating = models.FloatField(
        validators=[
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE)
        ]
    )

    image_url = models.URLField()

    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title