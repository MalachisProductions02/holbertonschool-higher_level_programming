#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure (list, dict, string, int, boolean)
for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Return the dictionary representation of an object
    with only serializable attributes.
    """
    return obj.__dict__.copy()
