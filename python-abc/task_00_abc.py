#!/usr/bin/env python3
"""Abstract Animal class and its subclasses Dog and Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class that implements Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that implements Animal."""

    def sound(self):
        return "Meow"
