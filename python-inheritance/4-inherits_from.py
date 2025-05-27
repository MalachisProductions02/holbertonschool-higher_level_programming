#!/usr/bin/python3
"""Function that checks if an object is an instance of a subclass of a_class."""

def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass (not exact class) of a_class."""
    return isinstance(obj, a_class) and type(obj) != a_class
