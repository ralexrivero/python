#!/usr/bin/env python3
""" inheritance """


class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

    def __str__(self):
        return "* Title: {}\n* Price: ${}\n* Period: {}\n* Publisher: {}\n\n{}\n".format(self.title, self.price, self.period, self.publisher, ("*"*80))

class Book(Publication):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

    def __str__(self):
        return "* Title: {}\n* Author: {}\n* Price: ${}\n* Pages: {}\n\n{}\n".format(b1.title, b1.author, b1.price, b1.pages, ("*"*80))


class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


b1 = Book("Harry Potter And The Philosopher's stone", 42.82, "J.K. Rowling", 432)

m1 = Magazine("People Magazine", 8.99, "Monthly", "PEOPLE")

n1 = Newspaper("The New York Times", 0.25, "Daily", "Times")

print(b1)

print(m1)

print(n1)