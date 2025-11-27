'''
File: Aviary.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure
class Aviary(Enclosure):
    def __init__(self, size, cleanliness,focus_animal = "Bird", environment_type= "Cage",  allowed_animal_type ="Bird", animal_list=[]):
        super.__init__(size, environment_type, cleanliness,focus_animal, allowed_animal_type, animal_list)

    def set_size(self, value):
        return self.size == 60

