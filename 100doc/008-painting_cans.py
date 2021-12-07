#!/usr/bin/env python3
from math import ceil
"""
Calculates the surface and the amount of cans to paint a wall
"""


def wall_surface(weight, height, cover):
    surface = (weight * height) / cover
    surface = ceil(surface)
    print("You will need {:d} cans of paint.".format(surface))


wall_weight = int(input("Weight of the wall: "))
wall_height = int(input("Height of the wall: "))
coverage = 5

wall_surface(weight=wall_weight, height=wall_height, cover=coverage)
