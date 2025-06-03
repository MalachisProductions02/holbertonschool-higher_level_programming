#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Defines a student by first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of the student.
        If attrs is a list of strings, only include those attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()
