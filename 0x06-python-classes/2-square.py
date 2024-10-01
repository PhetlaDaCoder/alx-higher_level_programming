#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Arguments:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("Size not an interger")
        elif size < 0:
            raise ValueError(" Size must be >= 0")
        self.__size = sizee
