#!/usr/bin/python3
"""Define attributes and method of function."""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of strings representing the available attributes and methods
        of the object.

    """
    return (dir(obj))
