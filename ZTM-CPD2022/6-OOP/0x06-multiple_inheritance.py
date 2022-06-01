#!/usr/bin/env python3
""" multiple inheritance """


class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print("{} is attacking with power of {}".format(self.name, self.power))


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print("{} is attacking with arrows: arrows left - {}".format(
            self.name, self.num_arrows))

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('boggie', 50, 100)
hb1.run()
hb1.check_arrows()
hb1.attack()
hb1.sign_in()
