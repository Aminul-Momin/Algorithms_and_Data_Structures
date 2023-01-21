"""A symbol table implemented with a separate-chaining hash table."""

from .sequential_search_st import SequentialSearchST


class SeperateChaininhHashST(object):
    """Implementation of unordered symbol table of  generic key-value pairs.

    The SequentialSearchST represents an unordered symbol table of
    key-value pairs. In the symbol table, when associating a value with a key
    that is already in the table, the convention is to replace the old value
    with the new value. Besides that it also hold the convention that a value
    con not be 'None'  - attempting to set a value associated with a key to
    None, deletes the key from the symbol table.
    """

    INIT_CAPACITY = 4

    def __init__(self):
        self.m = SeperateChaininhHashST.INIT_CAPACITY  # table size
        self.n = 0  # number of elements
        self.st = [None] * self.m  # table with m chains
        for i in range(self.m):
            self.st[i] = SequentialSearchST()

    def size(self):
        """Return number of elements stored in this Symbol table."""
        return self.n

    def is_empty(self):
        """Check whether this Symbol Table is empty or not"""
        return self.n == 0

    def get(self, key):
        """Return the value associate with the given key

        Args:
            key: the key to be searched.
        Returns:
            value associated with the given key if the key is in the table and
            None if the key is not in the table.
        """
        if key is None:
            raise ValueError("Can't search 'None' in the ST")
        i = self.hash(key)
        x = self.st[i].get(key)
        if x is None:
            return None
        return x

    def contains(self, key):
        """Check whether this Symbol Table contains the given key or not

        Args:
            key: the key to check if it is in the table
        Returns:
            True if the table contains the given key or False otherwise
        """
        if key is None:
            raise ValueError("Can't search 'None'")
        return self.get(key) is not None

    def _resize(self, chains):
        temp = SeperateChaininhHashST()
        temp.m = chains
        temp.st = [None] * temp.m
        for i in range(temp.m):
            temp.st[i] = SequentialSearchST()
        for i in range(self.m):
            for key in self.st[i].keys():
                temp.put(key, self.st[i].get(key))

        self.m = temp.m
        # self.n = temp.n
        self.st = temp.st

    def hash(self, key):
        h = abs(hash(key) % self.m)
        return h

    def put(self, key, value):
        """Inserts the key-value pair into the symbol table.

        It overwrites the old value with the new value if the key is already
        in the symbol table. If the value is 'None', this effectively deletes the
        key from the table.
        Args:
            key  : the key to be inserted into the table.
            value: value associated with the given key
        """
        if key is None:
            raise ValueError("Cannot insert 'None' into the table")
        if value is None:
            self.delete(key)
            return
        if self.n == 10 * self.m:
            self._resize(2 * self.m)

        i = self.hash(key)
        if not self.contains(key):
            self.n += 1
        self.st[i].put(key, value)

    def delete(self, key):
        """Removee the given key if it is in the symbol table.

        Args:
            key: the key to be removed
        """
        if key is None:
            raise ValueError("Cant' detele 'None' from the ST")
        if self.contains(key):
            self.n -= 1
        i = self.hash(key)
        self.st[i].delete(key)

        if self.m > SeperateChaininhHashST.INIT_CAPACITY and self.n <= 2 * self.m:
            self._resize(self.m // 2)

    def keys(self):
        """It collects and return all the keys in the symbol table.

        Returns:
            Iterable containing all the keys in the table
        """
        queue = []
        for chain in self.st:
            for key in chain.keys():
                queue.append(key)
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
        for i in range(self.m):
            for key in self.st[i]:
                yield key
