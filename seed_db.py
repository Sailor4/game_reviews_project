import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_catalog.settings')
django.setup()

from games.models import Game
from reviews.models import Review


def seed():
    print("Seeding database...")

    # 1. Create Games
    g1 = Game.objects.create(title="Elden Ring", platform="PC", genre="RPG", release_year=2022,
                             description="An epic open-world masterpiece.")
    g2 = Game.objects.create(title="Elden Ring", platform="Console", genre="RPG", release_year=2022,
                             description="The console version of the GOTY.")
    g3 = Game.objects.create(title="The Witcher 3", platform="PC", genre="RPG", release_year=2015,
                             description="Geralt's greatest adventure.")
    g4 = Game.objects.create(title="Cyberpunk 2077", platform="PC", genre="Action", release_year=2020,
                             description="Night City awaits.")
    g5 = Game.objects.create(title="Hades", platform="PC", genre="Roguelike", release_year=2020,
                             description="Escape the underworld.")
    g6 = Game.objects.create(title="Red Dead Redemption 2", platform="Console", genre="Action", release_year=2018,
                             description="The death of the Wild West.")
    g7 = Game.objects.create(title="Baldur's Gate 3", platform="PC", genre="RPG", release_year=2023,
                             description="Rolling a nat 20.")
    g8 = Game.objects.create(title="Diablo II Resurrected", platform="PC", genre="RPG", release_year=2021,
                             description="Classic hack and slash.")
    g9 = Game.objects.create(title="Diablo II Resurrected", platform="Console", genre="RPG", release_year=2021,
                             description="Classic hack and slash on the big screen.")
    g10 = Game.objects.create(title="Stardew Valley", platform="PC", genre="Simulation", release_year=2016,
                              description="A cozy farm life.")

    # 2. Create Reviews
    Review.objects.create(game=g1, reviewer_name="Gamer123", rating=10.0, content="Perfect game, best open world ever.")
    Review.objects.create(game=g1, reviewer_name="SoulsFan", rating=9.0, content="Hard but extremely rewarding.")
    Review.objects.create(game=g3, reviewer_name="CiriFan", rating=10.0,
                          content="The story is incredible even after all these years.")
    Review.objects.create(game=g4, reviewer_name="V", rating=7.5,
                          content="Much better after the updates, but still has issues.")
    Review.objects.create(game=g7, reviewer_name="D&D_Guy", rating=10.0,
                          content="The best RPG I have played in a decade.")
    Review.objects.create(game=g8, reviewer_name="OldSchool", rating=8.0,
                          content="Exactly how I remember it, but prettier.")
    Review.objects.create(game=g10, reviewer_name="RelaxedGamer", rating=9.5,
                          content="So peaceful, I play it every night.")

    print("Successfully added 10 games and 7 reviews")


if __name__ == "__main__":
    seed()