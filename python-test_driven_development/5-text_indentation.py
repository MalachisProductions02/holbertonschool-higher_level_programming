#!/usr/bin/python3
"""
This module defines a function that adds two new lines after '.', '?' and ':'.
"""

def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?' and ':'.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
