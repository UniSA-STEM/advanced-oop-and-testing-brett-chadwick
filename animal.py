from abc import ABC, abstractmethod

'''
File: animal.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Animal:
    def __init__(self, name, species, diet, category):
        self.name = name
        self.species = species
        self.diet = diet
        self.category = category

    @abstractmethod
    def make_noise(self):
        pass
    def eat_food(self):
        pass
    def sleep(self):
        pass

