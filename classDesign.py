# Parent class: Superhero
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from {self.universe}, and my power is {self.power}!"

    def use_power(self):
        return f"{self.name} uses their power: {self.power}!"

# Child class: FlyingHero
class FlyingHero(Superhero):
    def use_power(self):
        return f"{self.name} takes off and flies across the sky! 🦸‍♂️✨"

# Child class: StrengthHero
class StrengthHero(Superhero):
    def use_power(self):
        return f"{self.name} smashes with incredible strength! 💪💥"

# Creating instances
hero1 = FlyingHero("SkyWing", "Flight", "SkyVerse")
hero2 = StrengthHero("Titan", "Super Strength", "EarthRealm")

# Using methods
print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.use_power())
