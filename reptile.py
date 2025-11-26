"""
File: enclosure.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
class Reptile(Animal):
    """
    Initialization method, used to
    """
    def __init__(self, name, species, diet, hunger,rested,status ,cold_blooded = True, category = "Reptile"):
        super().__init__(name, species, diet, hunger, status, rested , category)
        self.cold_blooded = cold_blooded


    def make_noise(self):
        print(f"{self.name} hisses")

    def eat_food(self):
        return self.hunger == 100

    def sleep(self):
        return self.rested == True

    """
    str method to get and read 
    """
    def __str__(self):
        print(f"Name: {self.name}, Species: {self.species}, Diet: {self.diet}, Category: {self.category}, Hunger: {self.hunger}, Rested: {self.rested}, Cold Blooded: {self.cold_blooded}")


test = Reptile("Greg", 'Lizard', 'herbivore', hunger=75, rested=True)
test.make_noise()
print(test.__str__())


