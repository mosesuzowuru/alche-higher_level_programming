#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """A class that defines a rectangle by width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height

        Args:
            width: The width of the rectangle (default: 0)
            height: The height of the rectangle (default: 0)
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value: The new width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value: The new height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle, 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle

        Returns:
            String representation using print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return string representation to recreate the instance

        Returns:
            String that can be used with eval() to create new instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
