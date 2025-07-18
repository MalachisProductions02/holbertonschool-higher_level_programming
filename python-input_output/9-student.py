#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Defines a student by first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation for JSON serialization"""
        return self.__dict__.copy()
