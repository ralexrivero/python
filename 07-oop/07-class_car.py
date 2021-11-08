#!/usr/bin/env python3
"""
class car
"""
class Car:
    def __init__(self):
        self.brand = "Mercedes"
        self.year = 2021
        self.color = "Red"
        self.tires = 4
        self.on = False
    """ methods """
    def startCar(self, start):
        self.on = start
        """ if on == True """
        if(self.on):
            return "The car is running"
        else:
            return "The car is stopped"

    def __str__(self):
        return "Car properties\nBrand: {:s}\nYear: {:d}\nColor{:s}\nTires:{:d}\nOn:{}\n".format(self.brand, self.year, self.color, self.tires, self.on)

carOne = Car()
print(carOne.startCar(True))
print(str(carOne))