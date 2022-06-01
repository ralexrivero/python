#!/usr/bin/env python3
""" inheritance """


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print("{} is attacking with power of {}".format(self.name, self.power))


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print("{} is attacking with arrows: arrows left - {}".format(
            self.name, self.num_arrows))


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer("Robin", 100, 'robin@gmail.com')
print(wizard1)
wizard1.sign_in()
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(Wizard, User))  # false
print(isinstance(wizard1, object))
print(isinstance(Wizard, object))

for char in [wizard1, archer1]:
    char.attack()

print(wizard1.email)
print(archer1.email)

# introspection

print(dir(wizard1))
