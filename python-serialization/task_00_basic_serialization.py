#!/usr/bin/env python3
"""
Basic Serialization Module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary to JSON and saves it to a file.

    Args:
        data (dict): The data to serialize.
        filename (str): The name of the file to save the JSON into.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
