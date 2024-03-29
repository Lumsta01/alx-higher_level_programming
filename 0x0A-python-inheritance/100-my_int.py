#!/usr/bin/python3
"""Define class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """override == operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator."""
        return self.real == value
