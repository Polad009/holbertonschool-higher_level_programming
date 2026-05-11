#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing module"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Shape class"""

    @abstractmethod
    def area(self):
        """Abstract area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract perimeter method"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Returns area of circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
