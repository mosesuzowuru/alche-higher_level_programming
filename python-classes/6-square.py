#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square by its size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position

        Args:
            size: The size of the square (default: 0)
            position: The position of the square (default: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value: The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value: The new position value

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            The area of the square (size^2)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters with position offset"""
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for i in range(self.__position[1]):
            print()

        # Print the square with horizontal offset
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
