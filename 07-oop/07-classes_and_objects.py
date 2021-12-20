# Class and objects


class Jelly:
    # Init constructor to initilize the class
    def __init__(self, brand, flavor, color, size):
        self.brand = brand
        self.flavor = flavor
        self.color = color
        self.size = size

    def print_Jelly(self):
        print("The Jelly's brand: {:s} is flavor: {:s}, color: {:s} and size: {:s}".format(self.brand, self.flavor, self.color, self.size))


jelly1 = Jelly("Royarina", "Strawberry", "red", "medium")
jelly2 = Jelly("Royal", "Apple", "Green", "Big")

jelly1.print_Jelly()
jelly2.print_Jelly()
