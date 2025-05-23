#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (which are cast to integers).
    Raises:
        TypeError: if a or b is not an integer or float.
    Returns:
        int: The sum of a and b after casting to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
