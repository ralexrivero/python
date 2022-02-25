#!/usr/bin/env python3
""" create a class and instantiate to create objects """


class Player:
    """ create class Player """
    def __init__(self, name='anonymous', age=0):  # default parammeters
        membership = True  # class object attribute (is static)
        """
        __init__ magic method: init method
            is automatically called when instantiate
        self: refers to the instance
        name: this specific method
        """
        if age >= 18:
            self.name = name  # attribute (dynamic)
            self.age = age  # attribute

    def run(self):
        print('run!')
        return 'done'


""" must need to give a name and age to the object """
player01 = Player('Rony', 41)
player02 = Player('Alex', 18)


def printObj(obj):
    print('{}\nname: {}\nage: {}'.format(obj, obj.name, obj.age))


printObj(player01)
print('*'*10, '\n')
printObj(player02)

player01.run()
print(player01.run())

""" return the entire blueprint of the object """
help(player01)
