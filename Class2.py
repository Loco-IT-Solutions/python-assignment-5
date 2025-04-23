# Base class
class Superhero:
    def __init__(self, name, power_level):
        self.name = name
        self.__power_level = power_level  # encapsulated attribute

    def show_power(self):
        print(f"{self.name}'s power level is {self.__power_level}")

    def boost_power(self, amount):
        self.__power_level += amount
        print(f"{self.name}'s power has been boosted!")

# Inherited class
class Flyer(Superhero):
    def move(self):
        print(f"{self.name} is soaring through the skies! 🦅")

# Inherited class
class Swimmer(Superhero):
    def move(self):
        print(f"{self.name} is swimming through the ocean! 🌊")

# Create objects
hero1 = Flyer("SkyBolt", 85)
hero2 = Swimmer("WaveRider", 75)

hero1.show_power()
hero1.boost_power(10)
hero1.move()

hero2.show_power()
hero2.move()
