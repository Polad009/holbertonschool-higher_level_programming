#!/usr/bin/python3
"""
This module prints text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
