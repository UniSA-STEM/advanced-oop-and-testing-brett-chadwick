'''
File: vet.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import Staff
from animal import Animal
class Vet(Staff):
    def __init__(self,staffID, name, responsibilities, job ="Vet"):
        super().__init__(staffID, name, job, responsibilities)

    def conduct_health_check(self, health_check, animal):
        return health_check == True
