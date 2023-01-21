"""
This module contains implementation of an unordered, sequential-search,
doubly-linked list of  generic items.
"""

from ._nodes import DLLNode as Node, T
from typing import Iterable, Optional


# Testing is not done !!
class DLL():
    """Doubly Linked List of  generic items.

    The class represents an unordered list which support zero-based indexing.
    """
    def __init__(self, node=Node):
        self._head: Optional[node] = None  # head of the Linked List
        self._tail: Optional[node] = None  # head of the Linked List
        self._n: int = 0  # number of items in this linked list
        self._Node: Optional[node] = node

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def size(self) -> int:
        """Cmputes the number of items stored in this linked list.

        Returns:
            the number of items stored in this linked list.
        """
        return self._n

    def is_empty(self) -> bool:
        """Checks whether this linked list is empty or not.

        Returns:
            True if this list is empty, False otherwise.
        """
        return self._head is None and self._n == 0

    def contains(self, key: T) -> bool:
        """Checks if this list contains the specified key.

        Args:
            key: the key whose presence in this list is to be tested.
        Returns:
            True if the list contains the given key, False otherwise.
        """
        return self.index_of(key) != -1

    def prepend(self, key: T) -> None:
        """Add an item with the 'key' at the begining of this list.

        Args:
            key: the key of an item to be added.
        
        Raises:
            KeyError: if the given key is None.
        """
        if key is None: raise KeyError("invalid key !")
        self._head = self._Node(key, self._head, None)
        self._n += 1

    def append(self, key: T) -> None:
        """Add an item with 'key' at the end of this list.

        Args:
            key: the key of an item to be added.
        
        Raises:
            KeyError: if the given key is None.
        """
        if key is None: raise KeyError("invalid key !")
        self._tail = self._Node(key, None, self._tail)
        self._n += 1

    def insert(self, index: int, key: T) -> None:
        """Inserts an item with 'key' at specified index into this list.

        Args:
            index: index at which the item is to be added.
            key  : the key of the item to be added into this list.
            
        Raises:
            KeyError: if the given key is None.
            IndexError: if the given index is out of bound or None.
        """
        if key is None: raise KeyError("invalid key !")
        if index is None or index < 0 or index > self._n:
            raise IndexError("index out of bound !")
        if index == 0:
            return self.prepend(key)

        x = self._head
        while x is not None and index > 1:
            x = x._next
            index -= 1

        x._next = self._Node(key, x._next, x)
        self._n += 1

    def get_first(self) -> T:
        """Find the first item of this list.

        Returns:
            The key of the first item in this list.
            
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list !")
        return self._head._key

    def get_last(self) -> T:
        """Find the last item of this list.

        Returns:
            The key of the last item in this list.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list !")
        return self._tail._key

    def get(self, index: int) -> T:
        """Find the item at the specified index in this list.

        Args:
            index (int): index of the item to be returned.
        
        Returns:
            The key of item at the specified index in this list.
            
        Raises:
            IndexError: if the given index is out of bound or None.
        """
        if index is None or index < 0 or index > self._n - 1:
            raise IndexError("index out of bound !")

        x = self._head
        while (x is not None and index > 0):
            x = x._next
            index -= 1

        return x._key

    def index_of(self, key: T) -> int:
        """Find index of first occurance of specified key.

        Args:
            key: The key of which index to be found.
        
        Returns:
            Index of specified key if it's in this list, -1 otherwise.
        """
        x = self._head
        index = 0
        while (x is not None and key != x._key):
            x = x._next
            index += 1
        if x is None:
            return -1
        return index

    def poll(self) -> T:
        """Retrieves and removes the first item (head) of this list.

        Returns:
            The key of the first item in this list.
            
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list !")
        x = self._head._key
        self._head = self._head._next
        return x

    def peek(self) -> T:
        """Retrieves, without removing, the key of first item in this list.

        Returns:
            The key of the first item if this list is not empty, 'None'
            otherwise.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list !")
        return self._head._key

    def set_key(self, index: int, key: T) -> None:
        """Replaces the item at the given index by an item with 'key'.

        Args:
            index: index of the item to replace
            key  : the key of the item to be replaced by.
            
        Raises:
            IndexError: if the given index is out of bound or None.
        """
        if index is None or index < 0 or index > self.n - 1:
            raise IndexError("index out of bound !")
        if key is None: self.remove(index)

        if index == 0:
            self._head._key = key

        x = self._head
        while x._next is not None and index >= 1:
            x = x._next
            index -= 1

        x._key = key

    def delete(self, key: T) -> None:
        """Remove the first occurance of given key if it is in the list.

        Args:
            key : the key to be removed.
            
        Raises:
            KeyError: if the given key is None.
            RuntimeError: if this list is empty.
        """
        if key is None: raise KeyError("invalid key !")
        if self._head is None: RuntimeError("empty list !")

        if self._head and self._head._key == key:
            return self.remove_first()

        x = self._head._next
        while x is not None and x._key != key:
            x = x._next

        if x is not None:
            self._n -= 1
            x._prev._next = x._next
            x._next._prev = x._prev

    def remove_first(self) -> None:
        """Removes the head (first item) of this list.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list !")
        else:
            self._head = self._head._next
            self._n -= 1

    def remove(self, index: int) -> None:
        """Removes the item at the specified position in this list.

        Args:
            index (int): the index of the item to be removed.
            
        Raises:
            IndexError: if the given index is out of bound or None.
        """
        if index is None or index < 0 or index > self._n - 1:
            raise IndexError("index out of bound !")

        if index == 0:
            return self.remove_first()

        x = self._head
        i = 0

        while x is not None and i < index:
            x = x._next
            i += 1

        self._n -= 1
        x._prev._next = x._next
        x._next._prev = x._prev

    def remove_last(self) -> None:
        """Removes the last item from this list.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._tail is None: raise RuntimeError("empty list!")

        if self._tail._prev is None:
            return self.remove_first()

        self._tail = self._tail._prev
        self._tail._next = None
        self._n -= 1

    def items(self) -> Iterable[Node]:
        """It collects all the items of this List.

        Returns:
            Iterable containing all the items in the list.
        """
        queue = []
        x = self._head
        while x is not None:
            queue.append(x)
            x = x._next
        return queue

    def keys(self) -> Iterable[T]:
        """ It collects all the keys of items from the List.

        Returns:
            Iterable containing all the keys.
        """
        queue = []
        x = self._head
        while x is not None:
            queue.append(x._key)
            x = x._next
        return queue

    def __len__(self):
        return self.size()

    def __getitem__(self, idx: int) -> T:
        return self.get(idx)

    def __setitem__(self, idx: int, key: T) -> T:
        return self.set_key(idx, key)

    def __contains__(self, key: T) -> bool:
        return self.contains(key)

    def __delitem__(self, key: T):
        self.delete(key)

    def __iter__(self) -> T:
        x = self._head
        while x is not None:
            yield x._key
            x = x._next

    def __str__(self):
        iterator = []
        cur = self._head
        while cur:
            iterator.append(cur._key)
            cur = cur._next
        return ' -> '.join([str(i) for i in iterator])
