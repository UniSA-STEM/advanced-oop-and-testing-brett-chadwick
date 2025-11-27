'''
File: filename.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
import manager
from reptile import Reptile
from manager import Manager
while True:

    test = Reptile("Greg","Lizard", 'herbivore', 75,True, 1, "Nothing lol")
    test_lizard_1 = Reptile("Greg","Lizard", 'herbivore', 75,True, 2, "Nothing lol")
    test_lizard_2 = Reptile("Greg","Lizard", 'herbivore', 75,True, 3, "Nothing lol")

    animal_list_element =[test,test_lizard_1,test_lizard_2]
    animal_manager_list_element = []
    animal_manager_list_element.append(animal_list_element)
    print(animal_manager_list_element)
    testManager = manager.Manager(animal_manager_list_element)
    staff_list_element = []
    enclosure_list_element = []



