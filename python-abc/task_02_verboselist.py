#!/usr/bin/env python3
"""VerboseList: a subclass of list with added notifications for changes."""

class VerboseList(list):
    """A list subclass that prints messages on modifications."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print how many items were added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item from list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index, print a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
