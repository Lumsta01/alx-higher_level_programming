#!/usr/bin/python3
"""Define attributes added to object function."""


def add_attribute(obj, attr, value):
    """Adds new attribute to an object if possible.

    Args:
        obj(any): An object.
        attr(str): String representing the attribute name.
        value(any): Value of the attribute.

    Raises:
        TypeError: If the object can't have new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
