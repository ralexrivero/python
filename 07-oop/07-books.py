#!/usr/bin/env python3
class Books():
    """Book class docstring """
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        self._discount = amount
        """This underscore attribute is considered
        interal to the class"""

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}, Price: {}".format(self.title, self.author, self.pages, self.getprice())

class Newspaper():
    def __init__(self, title, publisher, month, year):
        self.title = title
        self.publisher = publisher
        self.month = month
        self.year = year

    def __str__(self):
        return "Title: {}, Publisher: {}, Month: {}, Year: {}".format(self.title, self.publisher, self.month, self.year)

news1 = Newspaper("The Morning", "The Times", "November", 2021)

book1 = Books("Python Rocks", "Ronald Rivero", 200, 39.99)
book2 = Books("Python for beginners", "Rodrigo Mato", 100, 49.99)

print(book1)
print(book1.author)
print(book1.title)
print(book1.pages)
print(book1.price)

print("Price: {:.2f}".format(book1.getprice()))
book1.setdiscount(0.10)
print("Final price: {:.2f}".format(book1.getprice()))

print(book1)
print("--")
print(book1.__dict__)

print(news1)

"""print type of two objects"""
print(type(news1))
print(type(book1))

"""Check if two objects are the same type"""
print(type(book1) == type(news1))

""" isinstance"""
print(isinstance(book1, Books))
print(isinstance(news1, Newspaper))
print(isinstance(book1, Newspaper))
print(isinstance(book1, object))

print(Books.__doc__)