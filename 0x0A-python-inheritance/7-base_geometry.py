#!/usr/bin/python3
"""define base geometry of class BaseGeometry."""


class BaseGeometry:
    """
    A class representing a geometric shape.

    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.

        Args:
            None

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value of an integer.

        Args:
            name (str): The name of the integer being validated.
            value (int): The value of the integer being validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
