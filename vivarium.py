'''
File: vivarium.py
Description: Child Class of enclosure class, Vivarium is apparently the name used for lizard housings.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure
from reptile import Reptile
class Vivarium(Enclosure):

    def __init__(self, size, environment_type, cleanliness,focus_animal="Lizard", allowed_animal_type="Lizard", enc_animal_list=[]):
        super().__init__( size, environment_type, cleanliness,focus_animal, allowed_animal_type, enc_animal_list)
    def add_animal_enc(self,animal):
        if animal.species == self.focus_animal:
            self.enc_animal_list.append(animal)
        else:
            print(f"{animal.species} is not allowed in this enclosure")
    def show_list(self):
        for i in self.enc_animal_list:
            print( f"{i}")

