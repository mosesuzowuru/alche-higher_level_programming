#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize a square with a given size

        Args:
            size: The size of the square (default: 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size^2)
        """
        return self.__size ** 2
