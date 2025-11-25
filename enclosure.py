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
    def __init__(self, size, environment_type, cleanliness, allowed_animal_type, animal_list=[]):
        self.size = size
        self.environment_type = environment_type
        self.cleanliness = cleanliness
        self.allowed_animal_type = allowed_animal_type
        self.animal_list = animal_list


    def get_size(self):
        return self._size

    def set_size(self, value):
        self._size = value


    def get_environment_type(self):
        return self._environment_type

    def set_environment_type(self, value):
        self._environment_type = value


    def get_cleanliness(self):
        return self._cleanliness

    def set_cleanliness(self, value):
        self._cleanliness = value


    def get_allowed_animal_type(self):
        return self._allowed_animal_type

    def set_allowed_animal_type(self, bool):
        self._allowed_animal_type = bool


    def get_animal_list(self):
        return self._animal_list

    def set_animal_list(self, value):
        self._animal_list = value

    def generate_report(self):
        pass



