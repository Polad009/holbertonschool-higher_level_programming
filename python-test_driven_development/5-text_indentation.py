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
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    for line in result.split("\n"):
        print(line.strip())
