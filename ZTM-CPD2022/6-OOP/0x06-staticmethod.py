#!/usr/bin/env python3


class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print("Hello i am {}".format(self.name))

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

player2 = PlayerCharacter('Tom', 20)
player3 = PlayerCharacter.adding_things(2, 3)
print(player2.adding_things)
print(player3)
