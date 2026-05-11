#!/usr/bin/python3
"""VerboseList module"""


class VerboseList(list):
    """A list subclass that prints notifications on modifications"""

    def append(self, item):
        """Appends item and prints notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends list and prints notification"""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes item and prints notification"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops item and prints notification"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
