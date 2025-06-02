#!/usr/bin/python3
"""
This module provides a function that returns the JSON representation
of a Python object (as a string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj: The object to convert.

    Returns:
        str: The JSON-formatted string.
    """
    return json.dumps(my_obj)
