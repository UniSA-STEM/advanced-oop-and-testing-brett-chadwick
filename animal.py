from abc import ABC, abstractmethod

'''
File: animal.py
Description: Animal class with abstract methods to be utilized by further animal child classes.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Animal(ABC):
    def __init__(self, name, species, diet, category, hunger, rested,status):
        self.name = name
        self.species = species
        self.diet = diet
        self.category = category
        self.hunger = hunger
        self.rested = rested
        self.status = status



    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

        # species
    def get_species(self):
        return self._species

        # diet
    def get_diet(self):
        return self._diet

        # hunger
    def get_hunger(self):
        return self._hunger

    def set_hunger(self, value):
        self._hunger = value

        # rested
    def get_rested(self):
        return self._rested

    def set_rested(self, value):
        self._rested = value

        # category
    def get_category(self):
        return self._category

    def set_category(self, value):
        self._category = value

    @abstractmethod
    def make_noise(self):
        pass

    @abstractmethod
    def eat_food(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def __str__(self):
        print (f"Name: {self.name}, Species: {self.species}, Diet: {self.diet}, Category: {self.category}, Hunger: {self.hunger}, Rested: {self.rested}, status: {self.status}")



