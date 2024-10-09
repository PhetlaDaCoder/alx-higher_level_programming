#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Stops user from instantiating a new LockedClass atrributes
    from anything but attributes called 'first_name;.
    """

    __slots__ = ["first_name"]
