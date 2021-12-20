#!/usr/bin/env python3
"""
creates a basic class
"""
class Book():
    def __init__(self, title):
        self.title = title

"""
creates instances of the class
"""

b1 = Book("Titanic") # create a Book object
b2 = Book("Lord of the Rings")

"""
print the class and property
"""

print(b1)
print(b1.title)