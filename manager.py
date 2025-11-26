'''
File: manager.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Manager:
    def __init__(self,animal_list = [], enclosure_list = [], staff_list = []):
        self.animal_list = animal_list
        self.enclosure_list = enclosure_list
        self.staff_list = staff_list
    def add_animal(self, animal):
        self.animal_list.append(animal)
    #adds new enclosure to enclosure list
    def add_enclosure(self, enclosure):
        self.enclosure_list.append(enclosure)
    #Adds Staff member to Staff list
    def add_staff(self, staff_member):
        self.staff_list.append(staff_member)

    def set_animal_hunger(self, animal, hunger):
        if hunger<70:
            animal.set_hunger(True)
        else:
            print(f"{animal} is not hungry yet.")

