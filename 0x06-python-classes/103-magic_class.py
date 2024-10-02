#!/usr/bin/python3

"""Defines a MagicClass matching a bytecode"""

import math 


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Initializes a MagicClass.

        Arg:
            radius (float or int): The radius of MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of MagicClass"""
        return (2 * math.pi * self.__radius)
