#!/usr/bin/python3}
"""
This module provides a function to read and print the contents of a UTF-8 text file.
"""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
