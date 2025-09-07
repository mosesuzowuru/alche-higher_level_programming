#!/usr/bin/python3
"""Module that contains Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square instance

        Args:
            size: The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
