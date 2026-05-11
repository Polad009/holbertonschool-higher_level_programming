#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
