#!/usr/bin/python3
"""8-rectangle module that defines a Rectangle class inheriting BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height (validated)."""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
