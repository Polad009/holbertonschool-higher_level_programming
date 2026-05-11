#!/usr/bin/python3
"""Search and replace module"""


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""
    return [replace if x == search else x for x in my_list]
