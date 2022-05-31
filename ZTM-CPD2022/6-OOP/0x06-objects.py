#!/usr/bin/env python3
""" OOP """


class PlayerCharacter:
    """ class PlayerCharacter """
    """ class object attribute, belongs to the class
        and doesn't change
    """
    membership = True

    def __init__(self, name='Anonymous', age=0):
        """ object attributes
        atuomatically called when instantiate the class
        dynamic and related to each object
        """
        self.name = name
        self.age = age
        # self refers to the object that will be created (playerOne)

    def run(self):
        print('run')

    def shout(self):
        print("My name is {}".format(self.name))


playerOne = PlayerCharacter('Harry', 43)
playerTwo = PlayerCharacter('Ronald', 41)
playerTwo.attack = 50
print('\nPlayerOne')
print(playerOne)
print(playerOne.name, playerOne.age)
playerOne.run()

print('\nPlayerTwo')
print(playerTwo.run())
print(playerTwo.attack)
playerTwo.run()

print()
""" help(playerOne)
help(type(playerOne)) """

print(playerOne.membership)

playerOne.shout()
playerTwo.shout()

playerThree = PlayerCharacter()
playerThree.run()
playerThree.shout()
print(playerThree.age)
