#!/usr/bin/python3
"""Dragon Mixins module"""


class SwimMixin:
    """Mixin that provides swim ability"""

    def swim(self):
        """Prints swimming message"""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides fly ability"""

    def fly(self):
        """Prints flying message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly"""

    def roar(self):
        """Prints roaring message"""
        print("The dragon roars!")
