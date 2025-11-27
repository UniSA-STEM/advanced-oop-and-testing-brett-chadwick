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
    def __init__(self,animalID, name, species, diet, category, hunger, status ,cold_blooded=True, isHungry=False, rested=True,):
        super().__init__(animalID, name, species, diet, category, hunger, status , isHungry, rested,)
        self.cold_blooded = cold_blooded


    def make_noise(self):
        print(f"{self.name} hisses")

    def eat_food(self):
        return self.hunger == 100

    def sleep(self):
        return self.rested == True

    def hangry(self):
        if self.hunger < 30:
            return

    """
    str method to get and read 
    """
    def __str__(self):
        print(f" Animal ID: {self.animalID} Name: {self.name}, Species: {self.species}, Diet: {self.diet}, Category: {self.category}, Hunger: {self.hunger}, Rested: {self.rested}"
              f", Cold Blooded: {self.cold_blooded} ,Status:{self.status} Is hungry: {self.isHungry}")





