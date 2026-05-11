#!/usr/bin/python3
"""Safe print integer module"""


def safe_print_integer(value):
    """Prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
