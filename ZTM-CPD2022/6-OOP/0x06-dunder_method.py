#!/usr/bin/env python3
""" dunder method """

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        """ basic costumization of a dunder method
            changing the default behavior """
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        """ give the object the super power to be called
        using () """
        return 'yess!'

    def __getitem__(self, i):
        """ acces item using brackets notation [] """
        return self.my_dict[i]

action_figure = Toy('red', 0)

# both are the same
print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))

# using call
print(action_figure())

# getitem using index
print(action_figure['name'])
