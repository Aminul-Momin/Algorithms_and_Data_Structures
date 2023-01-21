"""
This module contains implementation of an unordered, sequential-search,
singly-linked list of  generic items.
"""

from ._nodes import SLLNode as Node, T
from typing import Iterable, Optional, Generic


class SLL(Generic[T]):
    """Singly Linked List of  generic items.

    The class represents an unordered list which support 0-based indexing.
    """
    def __init__(self, a_list: Iterable[T] = None, node: Node = Node):
        self._head: Optional[node] = None  # head of the Linked List
        self._n: int = 0  # number of items in this linked list
        self._Node: Optional[node] = node

        if a_list:
            sll = SLL()
            for key in a_list:
                sll.append(key)
            self._head = sll._head

    @property
    def head(self):
        return self._head

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
        self._head = self._Node(key, self._head)
        self._n += 1

    def append(self, key: T) -> None:
        """Add an item with 'key' at the end of this list.

        Args:
            key: the key of an item to be added.
        
        Raises:
            KeyError: if the given key is None.
        """
        if key is None: raise KeyError("invalid key !")
        if self.is_empty():
            return self.prepend(key)

        x = self._head
        while x._next is not None:
            x = x._next
        x._next = self._Node(key)
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
            raise IndexError("index out of bound")
        if index == 0: return self.prepend(key)

        current = self._head
        while current and index > 1:
            current = current._next
            index -= 1

        current._next = self._Node(key, current._next)
        self._n += 1

    def set_key(self, index: int, key: T) -> None:
        """Replaces the item at the given index by an item with 'key'.

        Args:
            index: the index at which item to be replaced.
            key  : the key by which the item at 'index' to be replaced.
            
        Raises:
            IndexError: if the given index is out of bound or None.
        """
        if index is None or index < 0 or index > self.n - 1:
            raise IndexError("index out of bound !")
        if key is None:
            return self.remove(index)

        if index == 0:
            self._head._key = key

        current = self._head
        while current._next is not None and index >= 1:
            current = current._next
            index -= 1

        current._key = key

    def insert_before(self, before_key: T, key: T) -> None:
        """Inserts an new item with 'key' before 'before_key' into this list.

        Args:
            before_key: key before which new item with 'key' is to be added.
            key       : the key of new item to be added into this list.
            
        Raises:
            RuntimeError: if this list is empty.
            KeyError: if the given keys are None.
        """
        if self._head is None: raise RuntimeError("empty list !")
        if before_key is None or key is None: raise KeyError("invalid key")

        if self._head._key == before_key: return self.prepend(key)

        prev = self._head
        current = self._head._next

        while current:
            if current._key == before_key:
                prev._next = Node(key, current)
                self._n += 1
                return
            prev = current
            current = current._next

    def insert_after(self, after_key: T, key: T) -> None:
        """Inserts an new item with 'key' after 'after_key' into this list.

        Args:
            after_key: key after which new item with 'key' is to be inserted.
            key      : the key of new item to be inserted into this list.
            
        Raises:
            KeyError: if the given keys are None.
        """
        if after_key is None or key is None: raise KeyError("invalid key")

        current = self._head
        while current:
            if current._key == after_key:
                current._next = Node(key, current._next)
                self._n += 1
                return
            current = current._next

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
        return self.get(self._n - 1)

    def get(self, index: int) -> T:
        """Find the item at the specified index in this list.

        Args:
            index: index of the item in 0-based indexing.
        
        Returns:
            The key of item at the specified index in this list.
        
        Raises:
            IndexError: if the given index is out of bound or None.
        """
        if index is None or index < 0 or index > self._n - 1:
            raise IndexError("Index out of bound")

        x = self._head
        while (x is not None and index > 0):
            x = x._next
            index -= 1

        return x._key if x else None

    def index_of(self, key: T) -> int:
        """Find index of first occurance of specified key.

        Args:
            key: The key of which index to be found.
        
        Returns:
            Index of specified key if it's in this list, -1 otherwise.
        """
        x = self._head
        index = 0
        while (x and key != x._key):
            x = x._next
            index += 1

        return index if x else -1

    def poll(self) -> T:
        """Retrieves and removes the first item(head) of this list.

        Returns:
            The key of the first item in this list.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list!")
        x = self._head._key
        self._head = self._head._next
        return x

    def peek(self) -> T:
        """Retrieves, without removing, the first item in this list.

        Returns:
            The key of the first item if this list is not empty, 'None'
            otherwise.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list !")
        return self._head._key

    def delete(self, key: T) -> None:
        """Remove the first occurance of given key if it is in the list.

        Args:
            key : the key to be removed.
        
        Raises:
            KeyError: if the given key is None.
            RuntimeError: if this list is empty.
        """
        if key is None: raise KeyError("key is None")
        if self._head is None: raise RuntimeError("empty list !")

        if self._head and self._head._key == key: return self.remove_first()

        x = self._head._next
        prev = self._head
        while x is not None and x._key != key:
            prev = x
            x = x._next

        if x is not None:
            self._n -= 1
            prev._next = x._next

    def remove_first(self) -> None:
        """Removes the head (first item) of this list.
        
        Raises:
            RuntimeError: if this list is empty.
        
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
            IndexError: if specified index is out of bound.
        """
        if index is None or index < 0 or index > self._n - 1:
            raise IndexError("Index out of bound")

        if index == 0:
            return self.remove_first()

        x = self._head
        i = 0

        while x is not None and i < index - 1:
            x = x._next
            i += 1

        self._n -= 1
        x._next = x._next._next

    def remove_last(self) -> None:
        """Removes the last item from this list.
        
        Raises:
            RuntimeError: if this list is empty.
        """
        if self._head is None: raise RuntimeError("empty list!")
        if self._head._next is None: return self.remove_first()

        x = self._head
        while x._next._next:
            x = x._next

        x._next = None
        self._n -= 1

    def items(self) -> Iterable[Node]:
        """It collects all the items in the List.

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
        q = []
        cur = self._head
        while cur:
            q.append(cur._key)
            cur = cur._next
        return ' => '.join([f"({i})" for i in q])
