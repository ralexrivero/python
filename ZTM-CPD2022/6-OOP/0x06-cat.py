#!/usr/bin/env python3


class Cat:
    """ Cat class: """
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat01 = Cat('Milo', 10)
cat02 = Cat('Millo', 1)
cat03 = Cat('Tom', 7)


def oldestCat(*cats):
    """2 Create a function that finds the oldest cat"""
    oldest = 0
    for i in cats:
        if i.age > oldest:
            oldest = i.age
    return oldest


aged = oldestCat(cat01, cat02, cat03)
print("The oldest cat is {} years old".format(aged))
