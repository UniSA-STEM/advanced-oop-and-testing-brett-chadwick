from abc import ABC, abstractmethod
'''
File: staff.py
Description: A brief description of this Python module.
Author: Brett Chadwick
ID: 110407073
Username: chabx001
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Staff:
    """Declares the staff class attributes, uses staffID to display potential duplicate names."""

    def __init__(self, staffID, name, job, responsibilities):
        self.staffID = staffID
        self.name = name
        self.job = job
        self.responsibilities = responsibilities
        @abstractmethod
        def feed_animal(self):
            pass

        def clean_enclosure(self):
            pass

        def conduct_health_check(self):
            pass





