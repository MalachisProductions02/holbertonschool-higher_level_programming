#!/usr/bin/env python3
"""Dragon class using mixins for swim and fly abilities."""


class SwimMixin:
    """Mixin that adds swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon that can swim and fly, thanks to mixins."""

    def roar(self):
        print("The dragon roars!")
