#!/usr/bin/python3
"""Function that checks if an object is instance of a class or subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or inherits from it."""
    return isinstance(obj, a_class)
