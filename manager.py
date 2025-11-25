'''
File: manager.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Manager:
    def __init__(self,animal_list = [], enclosure_list = []):
        self.animal_list = animal_list
        self.enclosure_list = enclosure_list
    def add_animal(self, animal):
        self.animal_list.append(animal)
    def add_enclosure(self, enclosure):
        self.enclosure_list.append(enclosure)

    def set_animal_hunger(self, animal, hunger):
        if hunger<70:
            animal.set_hunger(True)
        else:

