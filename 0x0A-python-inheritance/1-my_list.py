#!/usr/bin/python3

"""
class MyList that inherits a list."""


class MyList(list):
    """A custom list class that adds a method for printing the sorted list"""

    def print_sorted(self):
        """Print the list, sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
