#!/usr/bin/python3
"""
This module provides a function that creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
