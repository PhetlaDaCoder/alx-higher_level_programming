#!/usr/bin/python3
"""Defines a function that prints a square."""


def print_square(size):
    """Prints a # character square.

    Arguments:
            size (int): The height or width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
