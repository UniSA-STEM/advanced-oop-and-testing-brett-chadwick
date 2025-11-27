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
from vivarium import Vivarium
bool_cont = True

test_lizard_enc = Vivarium("Small",'Lizard', 100)
test_lizard_1 = Reptile(1, "Greg", 'Lizard', "herbivore", "Small", 75, "Nothing",cold_blooded=True,isHungry=False,rested=True)
test_lizard_2 = Reptile(2, "Greg", 'Lizard', "herbivore", "Small", 75, "Nothing",cold_blooded=True,isHungry=False,rested=True)
test_lizard_3 = Reptile(3, "Greg", 'Lizard', "herbivore", "Small", 75, "Nothing",cold_blooded=True,isHungry=False,rested=True)
test_dragon_1 = Reptile(4, "steve", 'Dragon', "anything", "Massive", 75, "Nothing",cold_blooded=True,isHungry=False,rested=True)
animal_list_element =[test_lizard_1,test_lizard_2,test_lizard_3, test_dragon_1]
for i in range(len(animal_list_element)):
    print(f"Addeded{i}")
    test_lizard_enc.add_animal_enc(animal_list_element[i])
test_lizard_enc.show_list()

staff_list_element = []
enclosure_list_element = []



