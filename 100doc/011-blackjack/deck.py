#!/usr/bin/env python3


class Suits():
    def __init__(self, suit):
        self.values = ["clubs", "diamonds", "hearts", "spades"]


class Values():
    def __init__(self, values):
        self.suit = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}


class card(Suits, Values):
    def __init__(self, suit, value):
        
