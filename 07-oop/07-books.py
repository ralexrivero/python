#!/usr/bin/env python3
class Books():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Books("Python Rocks", "Ronald Rivero", 200)
book2 = Books("Python for beginners", "Rodirgo Mato", 100)

print(book1)
print(book1.author)
print(book1.title)
print(book1.pages)