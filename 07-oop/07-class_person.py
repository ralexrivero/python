#!/usr/bin/env python3
"""
Define class person
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personalData(self):
        print("Name: {:s}\nAge: {:d}\nGender: {:s}\n".format(self.name, self.age, self.gender))

Person001 = Person("Ronald", 41, "Male")
Person001.personalData()