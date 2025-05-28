#!/usr/bin/env python3
"""FlyingFish class using multiple inheritance from Fish and Bird."""


class Fish:
    """Base class representing a fish."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Base class representing a bird."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class that represents a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
