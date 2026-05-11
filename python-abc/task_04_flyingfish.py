#!/usr/bin/python3
"""FlyingFish module"""


class Fish:
    """Fish class"""

    def swim(self):
        """Prints swimming message"""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """Prints flying message"""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from Fish and Bird"""

    def fly(self):
        """Prints flying message"""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints swimming message"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints habitat message"""
        print("The flying fish lives both in water and the sky!")
