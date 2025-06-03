#!/usr/bin/python3
"""
This module provides a function that returns a Python object
from a JSON-formatted string.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
