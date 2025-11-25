"""
File: enclosure.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
class Mammal(Animal):
    """
    Initialization method, used to hardcode animaltype to avoid conflicts with other
    """
    def __init__(self, name, species, diet, hunger, rested = True, category = "Mammal"):
        super().__init__(name, species, diet, hunger, rested, category)

        # name



    def set_hunger(self):
        return self.hunger == 100
    def make_noise(self):
        print(f"{self.species} noises")

    def eat_food(self):
        return self.hunger == 100


    """
    Needs a modifier applied to further animal types to allow for them to not be on show while resting.
    """
    def sleep(self):
        return self.rested == True

    """
    str method to get and read 
    """
    def __str__(self):
        print(f"Name: {self.name}, Species: {self.species}, Diet: {self.diet}, Category: {self.category}, Hunger: {self.hunger}, Rested: {self.rested}")


test = Mammal("Greg", 'penguin', 'Carnivore', hunger=75, rested=True)
test.make_noise()
print(test.__str__())


