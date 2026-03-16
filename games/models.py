from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.db.models.aggregates import Avg

TITLE_MAX_LENGTH = 40
GENRE_MAX_LENGTH = 20
RATING_MIN_VALUE = 1
RATING_MAX_VALUE = 10.0
MIN_YEAR_CREATED = 1950
MAX_YEAR_CREATED = 2026
MIN_DESCRIPTION_LENGTH = 5
MAX_DESCRIPTION_LENGTH = 800


class Game(models.Model):
    PLATFORM_CHOICES = (
        ("Console", "Console"),
        ("PC", "PC"),
    )

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    platform = models.CharField(
        max_length=10,
        choices=PLATFORM_CHOICES
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH
    )

    release_year = models.IntegerField(
        validators=[MinValueValidator(MIN_YEAR_CREATED), MaxValueValidator(MAX_YEAR_CREATED)]
    )

    description = models.TextField(
        validators=[
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
            MaxLengthValidator(MAX_DESCRIPTION_LENGTH)
        ],
        help_text=f"description must be between {MIN_DESCRIPTION_LENGTH} and {MAX_DESCRIPTION_LENGTH} characters."
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)]
    )

    class Meta:
        unique_together = ("title", "platform")

    def get_calculated_rating(self): # work in progress, might not get finished till deadline :))
        average = self.review_set.aggregate(Avg('rating'))['rating__avg']

        if average:
            return round(average, 1)
        return "Not Rated Yet"

    def __str__(self):
        return f"{self.title} [{self.platform}]"