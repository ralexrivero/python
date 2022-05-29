#!/usr/bin/env python3
""" OOP """


class PlayerCharacter:
    """ class PlayerCharacter """
    def __init__(self, name, age):
        # atuomatically called when instantiate the class
        self.name = name
        self.age = age
        # self refers to the object that will be created (playerOne)

    def run(self):
        print('run')


playerOne = PlayerCharacter('Harry', 43)
playerTwo = PlayerCharacter('Ronald', 41)

print('PlayerOne')
print(playerOne)
print(playerOne.name, playerOne.age)
playerOne.run()

print('PlayerTwo')
print(playerTwo.run())
playerTwo.run()
