"""
This module contains implementation of FIFO queue using a Python list. It
supports the following operations.

size()
    Return the number of items in this queue.

is_empty()
    Return True if the Queue is empty, False otherwise.

enqueue(item)
    Add the given item into this queue.

dequeue()
    Remove and returns the item least recently added to this queue.

peek()
    Returns the item least recently added to this queue.

items():
    Returns an iterable containing all the items of this queue.

"""

from typing import TypeVar, Iterable

Item = TypeVar('Item')


class ResizingArrayQueue():
    """FIFO queue implementation using a Python list.

    This class provides basic functionality of a first-in-first-out (FIFO)
    queue of generic items. This implementation uses a resizing array
    abstraction, which double the underlying array when it is full and halves
    the underlying array when it is one-quarter full.
    The enqueue, dequeue, peek, size, and is-empty operations all take constant
    time in the worst case.
    """
    def __init__(self):

        self._q = [None] * 4  # Queue of elements.
        self._n = 0  # Number of elements on the queue.
        self._first = 0  # Index of the first element of the queue.
        self._last = 0  # Index of the next available slot on the queue.

    def size(self) -> int:
        """ Return the number of items in this queue."""
        return self._n

    def is_empty(self) -> bool:
        """ Return True if the Queue is empty, False otherwise."""
        return self._n == 0

    def enqueue(self, item: Item) -> None:
        """ Add the given item into this queue.

        Args:
        ----
            item : the item to be added to the queue
        """
        if len(self._q) == self._n: self._resize(2 * self._n)
        self._q[self._last] = item
        self._n += 1
        self._last += 1
        if self._last >= len(self._q): self._last = 0

    def dequeue(self) -> Item:
        """ Remove and returns the item least recently added to this queue.

        Returns:
        -------
            the item at the begining of this queue
        """
        item = self._q[self._first]
        self._q[self._first] = None
        self._n -= 1
        self._first += 1
        if self._first == len(self._q): self._first = 0
        if self._n > 0 and self._n == len(self._q) // 4:
            self._resize(len(self._q) // 2)
        return item

    def peek(self) -> Item:
        """ Returns the item least recently added to this queue.

        Returns:
        -------
            Returns the item least recently added to this queue.
        
        Raise:
        -----
            RuntimeError: if this queue is empty.
        """
        if self.is_empty(): raise RuntimeError("Queue underflowed")
        return self._q[self._first]

    def _resize(self, capacity) -> None:
        """ resize the underlying array to given capacity.

        Args:
        ----
            capacity : the capacity of the queue to be resized to
        """
        # assert capacity > self._n
        temp = [None] * capacity
        for i in range(self._n):
            temp[i] = self._q[(self._first + i) % len(self._q)]
        self._q = temp
        self._first = 0
        self._last = self._n

    def items(self) -> Iterable[Item]:
        """ Returns an iterable containing all the items of this queue.
        """
        items = [None] * self._n
        for i in range(self._n):
            items[i] = self._q[(self._first + i) % len(self._q)]
        return items

    def __len__(self):
        return self.size()

    def __delitem__(self, key):
        self.dequeue()

    def __iter__(self):
        for i in range(self._n):
            yield self._q[(self._first + i) % len(self._q)]
