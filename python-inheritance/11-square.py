#!/usr/bin/python3
"""11-square module.

Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with string representation and area calculation."""

    def __init__(self, size):
        """Initialize a Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
