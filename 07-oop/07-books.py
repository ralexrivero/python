#!/usr/bin/env python3
class Books():
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

book1 = Books("Python Rocks", "Ronald Rivero", 200, 39.99)
book2 = Books("Python for beginners", "Rodirgo Mato", 100, 49.99)

print(book1)
print(book1.author)
print(book1.title)
print(book1.pages)
print(book1.price)

print("Price: {:.2f}".format(book1.getprice()))
book1.setdiscount(0.10)
print("Final price: {:.2f}".format(book1.getprice()))