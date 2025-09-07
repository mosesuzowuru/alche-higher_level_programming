#!/usr/bin/python3
"""Module that contains BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): The name of the parameter
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
