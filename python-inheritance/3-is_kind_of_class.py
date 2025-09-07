#!/usr/bin/python3
"""Module that contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherited from it"""
    return isinstance(obj, a_class)
