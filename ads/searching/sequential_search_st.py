"""
An unordered symbol table implementation of key-value pairs.
"""


class SequentialSearchST:
    """Symbol table implementation using linked list.

    The SequentialSearchST represents an unordered symbol table of
    key-value pairs. In the symbol table, when associating a value with a key
    that is already in the table, the convention is to replace the old value
    with the new value. Besides that it also hold the convention that a value
    con not be 'None'  - attempting to set a value associated with a key to
    None, deletes the key from the symbol table.
    """

    # *************************** Nested Node Class ***************************#
    class Node:
        """Creates the inner Node class."""

        def __init__(self, key, value, nxt=None):
            self.key = key  # the key
            self.value = value  # the value associated with the key
            self.next = nxt  # the next linked sublist

    # ************************ End of Nested Node Class ***********************#

    def __init__(self):
        self.first = None  # head of the symbol table
        self.n = 0  # Total number of elements

    def size(self):
        """Return number of key-value pairs stored in this Symbol table."""
        return self.n

    def is_empty(self):
        """Check whether this Symbol Table is empty or not."""
        return self.n == 0 and self.first is None

    def contains(self, key):
        """Check whether this Symbol Table contains the given key or not.

        Args:
            key: the key to check if it is in the table
        Returns:
            True if the table contains the given key or False otherwise
        """
        return self.get(key) is not None

    def get(self, key):
        """Returns the value associated with given key or None if no such key.

        Args:
            key: the key of which value to be gotten
        
        Returns:
            value associated with the given key if the key is in the table and
            None if the key is not in the table.
        """
        if key is None:
            raise ValueError("Can't search 'None'")
        x = self._get(self.first, key)
        if x is None:
            return None
        return x.value

    def _get(self, x, key):
        """Return the subtree associate with the given key.

        Args:
            x  : the subtree
            key: the key with which a value is associated
        
        Returns:
            subtree corresponding to the given key if the key is in the table and
            None if the key is not in the symbol table.
        """
        while x is not None and key != x.key:
            x = x.next
        if x is None:
            return None
        return x

    def put(self, key, value):
        """Inserts the key-value pair into the symbol table.

        It overwrites the old value with the new value if the key is already
        in the symbol table. If the value is None, this effectively deletes the
        key from the table.

        Args:
            key  : the key given as string
            value: value associated with the given key
        """
        if key is None:
            raise ValueError("Can't insert 'None'")
        if value is None:
            self.delete(key)
        x = self.first
        while x is not None and key != x.key:
            x = x.next
        if x is not None:
            x.value = value
        else:
            self.first = self.Node(key, value, self.first)
            self.n += 1

    def delete(self, key):
        """Remove the given key if it is in the symbol table.

        Args:
            key: the key to be removed
        """
        if key is None:
            raise ValueError("Provided argument is None")
        self.first = self._delete(self.first, key)

    def _delete(self, x, key):
        """Remove the given key from the sublist, x.

        Args:
            x  : the subtries
            key: the key to be removed
        """
        if x is None:
            return
        elif key == x.key:
            self.n -= 1
            return x.next
        else:
            x.next = self._delete(x.next, key)
        return x

    def keys(self):
        """It collects and return all the keys in the symbol table.

        Returns:
            Iterable containing all the keys in the table
        """
        queue = []
        x = self.first
        while x is not None:
            queue.append(x.key)
            x = x.next
        return queue

    # ************************ Python Special Methods: ************************#
    def __len__(self):
        return self.size()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        x = self.first
        while x is not None:
            yield x.key
            x = x.next
