from abc import ABC, abstractmethod
'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Enclosure:
    def __init__(self, size, environment_type, cleanliness, animal_type, animal_list=[]):
        self.size = size
        self.environment_type = environment_type
        self.cleanliness = cleanliness
        self.animal_type = animal_type
        self.animal_list = animal_list

    def generate_report(self):
        pass



