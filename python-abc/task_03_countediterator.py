#!/usr/bin/env python3
"""CountedIterator: Tracks how many items have been iterated."""

class CountedIterator:
    """Custom iterator that counts the number of items returned."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return how many items have been iterated so far."""
        return self.count

    def __iter__(self):
        """Return the iterator itself (to support use in for-loops)."""
        return self
