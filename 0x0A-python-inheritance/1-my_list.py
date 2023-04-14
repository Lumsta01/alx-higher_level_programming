#!/usr/bin/python3
"""define class that contains MyList."""


class MyList(list):
    """Implement sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print sorted list in ascending order."""
        print(sorted(self))
