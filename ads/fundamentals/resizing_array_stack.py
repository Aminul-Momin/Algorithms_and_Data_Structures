"""
This module contains implementation of LIFO stack using a Python list. It
supports the following operations.

size()
    Return the number of items in this stack.

is_empty()
    Return True if the stack is empty, False otherwise.

push(item)
    Add the given item at the top of this Stack.

pop()
    Remove and return the item most recently pushed into this Stack

peek()
    Returns the item least recently added to this stack.

elements():
    Returns an iterable containing all the items of this stack.

"""

from typing import TypeVar, Iterable

Item = TypeVar('Item')


class ResizingArrayStack():
    """LIFO stack implementation using a Python list.

    This class provides basic functionality of a last-in-first-out (LIFO)
    Stack of generic items. This implementation uses a resizing array, which
    double the underlying array when it is full and halves the underlying array
    when it is one-quarter full.
    The push, pop, peek, size, and is-empty operations all take constant
    time in the worst case.

    """
    def __init__(self):

        self.stk = [None] * 4  # Stack of elements.
        self.n = 0  # Number of elements on the Stack.

    def size(self) -> int:
        ''' Return the number of items in this Stack'''
        return self.n

    def is_empty(self) -> bool:
        ''' Check if the Stack is empty.'''
        return self.n == 0

    def push(self, item) -> None:
        """Add the given item at the top of this Stack.

        Args:
        ----
            item : the item to be added to the stack
        """
        if self.n == len(self.stk):
            self._resize(2 * len(self.stk))
        self.stk[self.n] = item
        self.n += 1

    def pop(self) -> Item:
        """Remove and return the item most recently pushed into this Stack

        Returns:
        -------
            the item at the top of this stack
        """
        item = self.stk[self.n - 1]
        self.stk[self.n - 1] = None
        self.n -= 1
        if self.n > 0 and self.n == len(self.stk) // 4:
            self._resize(len(self.stk) // 2)
        return item

    def peek(self) -> Item:
        """Return the item most recently pushed into this Stack

        Returns:
        -------
            the item most recently pushed into this Stack.
        
        Raise:
        -----
            RuntimeError: if this queue is empty.
        """
        if self.is_empty(): raise RuntimeError("Stack underflowed")
        return self.stk[self.n - 1]

    def _resize(self, capacity) -> None:
        """resize the underlying array to given capacity

        Args:
        ----
            capacity : the capacity of the stack to be resized to
        """
        temp = [None] * capacity
        for i in range(self.n):
            temp[i] = self.stk[i]
        self.stk = temp

    def items(self) -> Iterable[Item]:
        """Returns an iterable containing all the items of this stack. """
        items = [None] * self.n
        for i in range(self.n):
            items[i] = self.stk[i]
        return items

    def __len__(self):
        return self.size()

    def __delitem__(self, key):
        self.pop()

    def __iter__(self):
        for i in range(self.n):
            yield self.stk[i]
