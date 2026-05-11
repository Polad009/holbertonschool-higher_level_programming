#!/usr/bin/python3
"""Abstract Animal Class module"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal class"""

    @abstractmethod
    def sound(self):
        """Abstract sound method"""
        pass


class Dog(Animal):
    """Dog subclass"""

    def sound(self):
        """Returns Bark"""
        return "Bark"


class Cat(Animal):
    """Cat subclass"""

    def sound(self):
        """Returns Meow"""
        return "Meow"
