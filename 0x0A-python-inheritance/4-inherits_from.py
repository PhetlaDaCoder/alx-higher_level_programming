#!/usr/bin/python3
"""Defines an inherited class_checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class 9type): The class to match the type of obj to check.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
