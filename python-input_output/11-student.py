#!/usr/bin/python3
"""Module that defines a Student class with serialization support."""


class Student:
    """Defines a student with attributes and JSON serialization methods."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of the student.
        If attrs is a list of strings, return only specified attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace attributes of the student instance from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
