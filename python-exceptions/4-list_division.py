#!/usr/bin/python3
"""Divide a list module"""


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(div)
    return result
