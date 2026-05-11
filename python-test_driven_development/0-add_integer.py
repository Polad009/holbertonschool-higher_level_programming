#!/usr/bin/python3
"""
This module adds 2 integers.

It provides a function add_integer that returns the sum of two integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.
    Returns an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
