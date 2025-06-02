#!/usr/bin/python3
"""
This module provides a function that appends a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file and returns the number of
    characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
