#!/usr/bin/python3
"""
Module contains the function inherits_from which checks
if an object is an instance of a subclass of a given class.
"""

def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass (not exact class) of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
