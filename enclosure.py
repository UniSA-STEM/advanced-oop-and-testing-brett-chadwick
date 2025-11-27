from abc import ABC, abstractmethod
'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Enclosure(ABC):
    def __init__(self, size, environment_type, cleanliness,focus_animal, allowed_animal_type, enc_animal_list=[]):
        self.size = size
        self.environment_type = environment_type
        self.cleanliness = cleanliness
        self.allowed_animal_type = allowed_animal_type
        self.enc_animal_list = enc_animal_list
        self.focus_animal = focus_animal


    def get_size(self):
        return self.size

    def set_size(self, value):
        self.size = value


    def get_environment_type(self):
        return self.environment_type

    def set_environment_type(self, value):
        self.environment_type = value


    def get_cleanliness(self):
        return self.cleanliness

    def set_cleanliness(self, value):
        self.cleanliness = value

    def get_animal_list(self):
        return self.enc_animal_list
    # gets new animal added to enclosure and adds to list.

    #animal_addition = animal.Animal()
    #if animal_addition.si ==:
    @abstractmethod
    def add_animal_enc(self,animal):
     pass



