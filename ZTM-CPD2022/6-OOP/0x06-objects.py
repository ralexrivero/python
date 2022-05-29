#!/usr/bin/env python3
""" OOP """


class PlayerCharacter:
    """ class PlayerCharacter """
    def __init__(self, name):
        # atuomatically called when instantiate the class
        self.name = name
        # self refers to the object that will be created (playerOne)

    def run(self):
        print('run')


playerOne = PlayerCharacter('Harry')
playerTwo = PlayerCharacter('')
print(playerOne)
print(playerOne.name)
playerOne.run()
