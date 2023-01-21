from typing import Generic, Iterable, Optional
from ._nodes import T, SLLNode as Node


class Stack(Generic[T]):
    """The Stack class represents a last-in-first-out (LIFO) stack of generic
    items.

    This implementation uses a singly linked list with a class for linked-list
    nodes.

    """
    def __init__(self, a_list: Iterable[T] = None, node: Node = Node):
        self._head: Optional[node] = None  # head of the Linked List
        self._n: int = 0  # number of items in this stack
        self._Node: Optional[node] = node

        if a_list:
            stk = Stack()
            for key in a_list:
                stk.append(key)
            self._head = stk._head

    def size(self) -> int:
        """Cmputes the number of items stored in this stack.

        Returns:
            the number of items stored in this stack.
        """
        return self._n

    def is_empty(self) -> bool:
        """Checks whether this stack is empty or not.

        Returns:
            True if this stack is empty, False otherwise.
        """
        return self._head is None and self._n == 0

    def contains(self, key: T) -> bool:
        """Checks if this stack contains the specified key.

        Args:
            key: the key whose presence in this stack is to be tested.
        Returns:
            True if the list contains the given key, False otherwise.
        """
        return self.index_of(key) != -1

    def push(self, key: T) -> None:
        """Add an item with the 'key' into this stack.

        Args:
            key: the key of an item to be added.
        """
        if key is None:
            raise KeyError("can't push 'None'")
        self._head = self._Node(key, self._head)
        self._n += 1

    def pop(self) -> T:
        """Retrieves and removes the last item added into this stack.

        Returns:
            the last item added into this stack.
        """
        if self._head is None:
            raise RuntimeError("remove_last() was called on empty list!")
        x = self._head._key
        self._head = self._head._next
        return x

    def peek(self) -> T:
        """Retrieves, without removing, the last item added into this stack.

        Returns:
            the last item added if this stack is not empty, 'None' otherwise.

        """
        return self._head._key if self._head is not None else None

    def items(self) -> Iterable[T]:
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

    def __contains__(self, key: T) -> bool:
        return self.contains(key)

    def __delitem__(self):
        self.pop()

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
