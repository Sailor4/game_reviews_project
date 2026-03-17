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
    g11 = Game.objects.create(title="God of War", platform="PC", genre="Action", release_year=2022,
                              description="A father and son journey through Norse mythology.")
    g12 = Game.objects.create(title="God of War", platform="Console", genre="Action", release_year=2018,
                              description="The masterpiece that reinvented Kratos.")
    g13 = Game.objects.create(title="Horizon Zero Dawn", platform="PC", genre="Action", release_year=2020,
                              description="Fight robotic dinosaurs in a lush post-apocalyptic world.")
    g14 = Game.objects.create(title="Resident Evil Village", platform="Console", genre="Horror", release_year=2021,
                              description="Survival horror at its finest in a creepy European village.")
    g15 = Game.objects.create(title="Civilization VI", platform="PC", genre="Strategy", release_year=2016,
                              description="Build an empire that stands the test of time.")
    g16 = Game.objects.create(title="Forza Horizon 5", platform="PC", genre="Racing", release_year=2021,
                              description="Open-world racing across the vibrant landscapes of Mexico.")
    g17 = Game.objects.create(title="Forza Horizon 5", platform="Console", genre="Racing", release_year=2021,
                              description="Stunning 4K racing on the big screen.")
    g18 = Game.objects.create(title="Hollow Knight", platform="PC", genre="Metroidvania", release_year=2017,
                              description="A challenging and beautiful 2D adventure in a ruined bug kingdom.")
    g19 = Game.objects.create(title="Bloodborne", platform="Console", genre="RPG", release_year=2015,
                              description="Fear the Old Blood in this gothic horror action RPG.")
    g20 = Game.objects.create(title="Half-Life: Alyx", platform="PC", genre="Action", release_year=2020,
                              description="The definitive VR experience set between HL1 and HL2.")
    g21 = Game.objects.create(title="Apex Legends", platform="PC", genre="Battle Royale", release_year=2019,
                              description="A high-octane battle royale where legendary characters with powerful abilities team up to battle for fame and fortune on the fringes of the Frontier. It features a unique ping system and fluid movement mechanics that set it apart from its competitors.")
    g22 = Game.objects.create(title="Apex Legends", platform="Console", genre="Battle Royale", release_year=2019,
                              description="The console version of the hit hero-shooter. Optimized for controllers with high-aim assist settings and smooth performance on next-gen hardware, allowing for intense competitive play in the living room.")
    g23 = Game.objects.create(title="Skyrim: Special Edition", platform="PC", genre="RPG", release_year=2016,
                              description="Winner of more than 200 Game of the Year Awards, Skyrim Special Edition brings the epic fantasy to life in stunning detail. The PC version is legendary for its massive modding community, allowing players to transform the game into almost anything they can imagine.")
    g24 = Game.objects.create(title="Skyrim: Special Edition", platform="Console", genre="RPG", release_year=2016,
                              description="Experience the complete Elder Scrolls journey on your console. This edition includes the critically acclaimed game and add-ons with all-new features like remastered art and effects, volumetric god rays, and dynamic depth of field.")
    g25 = Game.objects.create(title="Portal 2", platform="PC", genre="Puzzle", release_year=2011,
                              description="The single-player portion of Portal 2 introduces a cast of dynamic new characters, a host of fresh puzzle elements, and a much larger set of devious test chambers. Players will explore never-before-seen areas of the Aperture Science Labs and face off against GLaDOS once again.")
    g26 = Game.objects.create(title="The Last of Us Part II", platform="Console", genre="Action", release_year=2020,
                              description="Five years after their dangerous journey across the post-pandemic United States, Ellie and Joel have settled down in Jackson, Wyoming. A violent event disrupts that peace, and Ellie embarks on a relentless journey to carry out justice and find closure.")
    g27 = Game.objects.create(title="Minecraft", platform="PC", genre="Simulation", release_year=2011,
                              description="The ultimate sandbox experience. Explore infinitely generated worlds and build everything from the simplest of homes to the grandest of castles. Play in creative mode with unlimited resources or mine deep into the world in survival mode, crafting weapons and armor to fend off dangerous mobs.")
    g28 = Game.objects.create(title="Minecraft", platform="Console", genre="Simulation", release_year=2011,
                              description="Minecraft on console brings the same creative freedom to your TV. Featuring split-screen play for up to four players, it's the perfect way to build and explore with friends from the comfort of your couch.")
    g29 = Game.objects.create(title="Sekiro: Shadows Die Twice", platform="PC", genre="Action", release_year=2019,
                              description="In Sekiro: Shadows Die Twice you are the 'one-armed wolf', a disgraced and disfigured warrior rescued from the brink of death. Explore late 1500s Sengoku Japan, a brutal period of constant life and death conflict, as you come face to face with larger than life foes in a dark and twisted world.")
    g30 = Game.objects.create(title="Doom Eternal", platform="PC", genre="Action", release_year=2020,
                              description="Hell's armies have invaded Earth. Become the Slayer in an epic single-player campaign to conquer demons across dimensions and stop the final destruction of humanity. The only thing they fear... is you. Experience the ultimate combination of speed and power with the next leap in push-forward, first-person combat.")
    g31 = Game.objects.create(title="BioShock Infinite", platform="PC", genre="Action", release_year=2013,
                              description="Indebted to the wrong people, private investigator Booker DeWitt must travel to the flying city of Columbia to rescue a mysterious woman named Elizabeth. They form a powerful bond as they fight to escape a city that is literally falling from the sky.")
    g32 = Game.objects.create(title="BioShock Infinite", platform="Console", genre="Action", release_year=2013,
                              description="The breathtaking journey to the city of Columbia, optimized for console play. Experience the sky-line combat mechanics and the emotional story of Booker and Elizabeth in this remastered edition for modern hardware.")
    g33 = Game.objects.create(title="It Takes Two", platform="PC", genre="Puzzle", release_year=2021,
                              description="An innovative co-op adventure where two players take on the roles of a clashing couple turned into dolls by a magic spell. Trapped in a fantastical world where the unpredictable hides around every corner, they must work together to save their fractured relationship.")
    g34 = Game.objects.create(title="It Takes Two", platform="Console", genre="Puzzle", release_year=2021,
                              description="The ultimate couch co-op experience. Winner of Game of the Year, this title requires two players to work in perfect harmony to overcome diverse challenges that blend narrative and gameplay in ways never seen before.")
    g35 = Game.objects.create(title="Dead Space", platform="PC", genre="Horror", release_year=2023,
                              description="A sci-fi survival horror classic rebuilt from the ground up to offer a deeper, more immersive experience. Isaac Clarke is an everyman engineer on a mission to repair a vast mining ship, only to find the crew has been slaughtered and infected by alien scourges.")
    g36 = Game.objects.create(title="Street Fighter 6", platform="PC", genre="Fighting", release_year=2023,
                              description="The latest entry in the legendary fighting game series. Powered by Capcom’s proprietary RE ENGINE, the experience spans three distinct game modes: Fighting Ground, World Tour, and Battle Hub. It redefines the genre with a highly evolved combat system.")
    g37 = Game.objects.create(title="Street Fighter 6", platform="Console", genre="Fighting", release_year=2023,
                              description="Take the fight to the big screen. Street Fighter 6 offers a revolutionary modern control scheme that allows new players to jump straight into the action while keeping the classic inputs for the seasoned fighting game veterans.")
    g38 = Game.objects.create(title="RimWorld", platform="PC", genre="Simulation", release_year=2018,
                              description="A sci-fi colony sim driven by an intelligent AI storyteller. Generates stories by simulating psychology, ecology, gunplay, melee combat, climate, biomes, diplomacy, interpersonal relationships, art, medicine, trade, and more.")
    g39 = Game.objects.create(title="Disco Elysium", platform="PC", genre="RPG", release_year=2019,
                              description="A groundbreaking open-world role-playing game. You’re a detective with a unique skill system at your disposal and a whole city block to carve your path across. Interrogate unforgettable characters, crack murders, or take bribes. Become a hero or an absolute disaster of a human being.")
    g40 = Game.objects.create(title="Outer Wilds", platform="PC", genre="Adventure", release_year=2019,
                              description="An open-world mystery about a solar system trapped in an endless time loop. As the newest recruit of Outer Wilds Ventures, you’ll explore a solar system that changes over time, visiting planets that crumble beneath your feet or are swallowed by sand.")


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
    Review.objects.create(game=g11, reviewer_name="NeonSamurai", rating=9.5,
                          content="God of War on PC is a technical marvel. The transition from the Greek era to Norse mythology is handled with such emotional depth, and the combat feels heavy and impactful with every swing of the Leviathan Axe.")
    Review.objects.create(game=g12, reviewer_name="ConsoleKing", rating=10.0,
                          content="This is the game that defined the last generation. The single-shot camera technique is breathtaking, and seeing the bond grow between Kratos and Atreus is one of the best storytelling moments in gaming history.")
    Review.objects.create(game=g13, reviewer_name="PixelCollector", rating=8.5,
                          content="Horizon Zero Dawn features one of the most unique settings I've ever explored. Hunting giant robotic dinosaurs with a bow and arrow never gets old, and the mystery of what happened to the 'Old Ones' is genuinely intriguing.")
    Review.objects.create(game=g18, reviewer_name="QuestLog", rating=10.0,
                          content="Hollow Knight is a masterpiece of atmosphere and level design. The world of Hallownest is so dense with secrets that I'm still finding new areas after 40 hours of gameplay. It's difficult, but extremely fair.")
    Review.objects.create(game=g19, reviewer_name="NeonSamurai", rating=10.0,
                          content="Bloodborne is perfection. The fast-paced, aggressive combat system is much more exciting than Dark Souls, and the shift from Victorian gothic horror into Lovecraftian nightmares is absolutely brilliant.")
    Review.objects.create(game=g20, reviewer_name="V", rating=9.0,
                          content="Half-Life: Alyx is a glimpse into the future of gaming. The level of interactivity in VR is mind-blowing—I spent ten minutes just drawing on a window with a marker. It's the best Half-Life story in years.")
    Review.objects.create(game=g23, reviewer_name="PixelCollector", rating=9.0,
                          content="I've been playing Skyrim for over a decade and the modding community on PC keeps it feeling fresh every single year. It is the ultimate role-playing sandbox where you can truly be anyone and do anything.")
    Review.objects.create(game=g25, reviewer_name="QuestLog", rating=10.0,
                          content="Portal 2 has some of the best writing and voice acting ever seen in a video game. The puzzles are perfectly paced, but it's the banter between GLaDOS and Wheatley that makes it an absolute must-play.")
    Review.objects.create(game=g26, reviewer_name="NeonSamurai", rating=6.5,
                          content="The Last of Us Part II is technically impressive and the acting is top-tier, but the story is incredibly polarizing. I appreciated the risks Naughty Dog took, but some of the narrative choices felt unnecessarily cruel.")
    Review.objects.create(game=g27, reviewer_name="Gamer123", rating=10.0,
                          content="Minecraft is the only game where the only limit is your own imagination. Whether you're building a simple dirt shack or a fully functional computer out of redstone, there's a meditative quality to the gameplay.")
    Review.objects.create(game=g29, reviewer_name="SoulsFan", rating=9.5,
                          content="Sekiro is the most focused combat system FromSoftware has ever created. Once the 'clashing swords' rhythm clicks, it feels more like a dance than a fight. Defeating the final boss was the proudest moment of my gaming life.")
    Review.objects.create(game=g30, reviewer_name="OldSchool", rating=9.0,
                          content="Doom Eternal is combat chess at 200 miles per hour. It forces you to use every tool in your arsenal to survive, and the soundtrack is enough to make you feel like an unstoppable force of nature.")
    Review.objects.create(game=g33, reviewer_name="PixelCollector", rating=10.0,
                          content="It Takes Two is the most creative co-op game I've ever played. Every single level introduces a brand new mechanic that could be its own game, and the story actually has a lot of heart.")
    Review.objects.create(game=g38, reviewer_name="QuestLog", rating=8.5,
                          content="RimWorld is a story generator first and a colony sim second. I've had colonies fail because a pet squirrel went insane, and I've had colonies thrive through organ harvesting. It's chaotic and wonderful.")
    Review.objects.create(game=g39, reviewer_name="NeonSamurai", rating=10.0,
                          content="Disco Elysium is the best-written game I have ever played. It's essentially a massive interactive novel about philosophy, politics, and failure. The internal dialogue system is a stroke of genius.")
    Review.objects.create(game=g40, reviewer_name="SoulsFan", rating=10.0,
                          content="Outer Wilds is a game you can only truly play once. The sense of discovery as you piece together the mystery of the universe is unmatched. Please, go into this game knowing as little as possible.")
    Review.objects.create(game=g35, reviewer_name="V", rating=9.0,
                          content="The Dead Space remake is how you do a remake right. It honors the original while expanding the ship and making the Necromorphs even more terrifying. The sound design is absolutely bone-chilling.")
    Review.objects.create(game=g36, reviewer_name="Gamer123", rating=8.5,
                          content="Street Fighter 6 is the most accessible fighting game in years. The modern controls are great for beginners, but the drive gauge system adds so much tactical depth for high-level players.")
    Review.objects.create(game=g21, reviewer_name="NeonSamurai", rating=8.0,
                          content="Apex Legends has the best movement of any Battle Royale on the market. The character abilities create a lot of strategic variety, but the microtransactions are getting a bit out of hand lately.")
    Review.objects.create(game=g15, reviewer_name="QuestLog", rating=9.0,
                          content="Civilization VI is the ultimate 'just one more turn' game. I started playing at 8 PM and suddenly it was 4 AM. The district system adds a great layer of city-planning strategy.")
    Review.objects.create(game=g5, reviewer_name="NeonSamurai", rating=10.0,
                          content="Hades is the gold standard for roguelikes. The way the narrative progresses even when you die makes every run feel meaningful. The voice acting and art style are simply unmatched in the indie scene.")
    Review.objects.create(game=g14, reviewer_name="HorrorAddict", rating=8.0,
                          content="Resident Evil Village is a wild ride. It feels like a 'Greatest Hits' of the series, blending the action of RE4 with the atmosphere of RE7. Lady Dimitrescu is an iconic villain, even if her segment is a bit short.")
    Review.objects.create(game=g16, reviewer_name="PetrolHead", rating=9.0,
                          content="Forza Horizon 5 is the most beautiful racing game ever made. Mexico is a diverse and massive playground, and the sheer number of cars and events is overwhelming in the best way possible.")
    Review.objects.create(game=g31, reviewer_name="StorySeeker", rating=9.5,
                          content="BioShock Infinite is a masterpiece of world-building. The city of Columbia is breathtaking, and the relationship between Booker and Elizabeth is the heart of the game. That ending still leaves me speechless years later.")
    Review.objects.create(game=g34, reviewer_name="CoopBuddy", rating=10.0,
                          content="If you have a partner or a friend to play with, It Takes Two is mandatory. I've never seen a game change its core mechanics so frequently and successfully. It's pure joy from start to finish.")
    Review.objects.create(game=g2, reviewer_name="QuestLog", rating=5.0,
                          content="The console version of Elden Ring is amazing, but the performance on older hardware is disappointing. I experienced several frame drops during boss fights which made an already hard game feel unfair.")
    Review.objects.create(game=g13, reviewer_name="NeonSamurai", rating=4.0,
                          content="I really wanted to like Horizon on PC, but the port was a mess at launch. Constant crashes and stuttering ruined the immersion for me. Stick to the console version if you can.")
    Review.objects.create(game=g22, reviewer_name="PixelCollector", rating=7.0,
                          content="Apex on console is fun, but the aim assist feels a bit too strong compared to PC play. It’s still a top-tier shooter, but the competitive balance feels slightly off depending on your platform.")
    Review.objects.create(game=g32, reviewer_name="QuestLog", rating=9.0,
                          content="The BioShock Infinite remaster for consoles looks crisp. Flying through the air on sky-lines feels even better at 60fps. A great way to experience a classic if you missed it the first time.")
    Review.objects.create(game=g37, reviewer_name="FighterX", rating=9.5,
                          content="Street Fighter 6 on console is the definitive way to play. The input lag is non-existent on next-gen, and the World Tour mode is a surprisingly deep RPG-like experience for fighting game fans.")
    Review.objects.create(game=g8, reviewer_name="OldSchool", rating=4.5,
                          content="Diablo II Resurrected looks great, but the lobby system on PC is a step backward from the original. Trying to find games with friends is more frustrating than it was twenty years ago.")
    Review.objects.create(game=g6, reviewer_name="WesternGuy", rating=10.0,
                          content="Red Dead Redemption 2 is the most detailed open world ever created. The slow pace isn't for everyone, but if you want to lose yourself in a living, breathing world, this is the pinnacle of the genre.")
    Review.objects.create(game=g15, reviewer_name="NeonSamurai", rating=8.5,
                          content="Civilization VI is still the king of 4X strategy. The 'Gathering Storm' expansion added so much depth with the climate system. It’s a game I’ll probably still be playing in 2030.")
    Review.objects.create(game=g28, reviewer_name="PixelCollector", rating=9.0,
                          content="Minecraft on console has come a long way. The bedrock edition allows me to play with my friends on PC and mobile, making it the ultimate social gaming experience for the family.")
    Review.objects.create(game=g11, reviewer_name="SoulsFan", rating=10.0,
                          content="God of War (2018) changed what I thought an action game could be. The combat is incredibly satisfying, but it's the maturity of the writing that really stayed with me.")
    Review.objects.create(game=g17, reviewer_name="PetrolHead", rating=9.0,
                          content="The console version of Forza 5 is a technical showpiece. Running this in 4K on a big screen is a treat for the eyes. It's the best reason to own a next-gen console right now.")
    Review.objects.create(game=g18, reviewer_name="NeonSamurai", rating=9.0,
                          content="Hollow Knight's soundtrack alone is worth the price. It's a hauntingly beautiful game that rewards exploration like no other Metroidvania. It's tough, but the atmosphere keeps you coming back.")
    Review.objects.create(game=g40, reviewer_name="PixelCollector", rating=10.0,
                          content="Outer Wilds is the only game that made me feel like a real archeologist. Piecing together a dead civilization's history to save the future is a feeling no other game has captured.")
    Review.objects.create(game=g24, reviewer_name="QuestLog", rating=8.0,
                          content="Skyrim on console is still a blast. While you don't get the crazy mods of the PC version, the stability and ease of play on the couch make it my preferred way to get lost in Tamriel.")
    Review.objects.create(game=g21, reviewer_name="Gamer123", rating=8.5,
                          content="Apex Legends is the king of movement shooters. The ping system is so good that I don't even need a mic to coordinate with random teammates. Constant updates keep the meta fresh.")
    Review.objects.create(game=g3, reviewer_name="NeonSamurai", rating=10.0,
                          content="The Witcher 3 is still the benchmark for side-quest design. Every small contract feels like a fully fleshed-out story with difficult moral choices. A true masterpiece of the genre.")
    Review.objects.create(game=g1, reviewer_name="QuestLog", rating=10.0,
                          content="Elden Ring is the culmination of everything FromSoftware has learned over the last decade. The sense of scale is terrifying, and the freedom to go anywhere is exhilarating.")
    Review.objects.create(game=g4, reviewer_name="CyberPunk88", rating=8.0,
                          content="Cyberpunk 2077 is finally the game it was promised to be. Night City is gorgeous, the story is gripping, and the 2.0 update fixed almost every major complaint I had at launch.")

    print("Successfully added 40 games and 50 reviews")


if __name__ == "__main__":
    seed()