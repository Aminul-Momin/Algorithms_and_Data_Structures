"""
A symbol table implemented with a linear-probing hash table. It supports the 
following operations. 

size()
    Return number of elements stored in this Symbol table.

is_empty()
    Check whether this Symbol Table is empty or not

get(key)
    Return the value associate with the given key

contains(key)
    Check whether this Symbol Table contains the given key or not

put(key, value)
    Inserts the key-value pair into the symbol table, overwriting the
    old value with the new value if the key is already in the symbol table.
    If the value is None, this effectively deletes the key from the table.

delete(key)
    Removee the given key if it is in the symbol table.

keys_set()
    It collects and return all the keys in the symbol table.

"""


class LinearProbingHashST(object):
    """Implementation of unordered symbol table of  generic key-value pairs.

    The LinearProbingHashST represents an unordered symbol table of  generic
    key-value pairs. In the symbol table, when associating a value with a key
    that is already in the table, the convention is to replace the old value
    with the new value. Besides that it also hold the convention that a value
    con not be 'None'  - attempting to set a value associated with a key to
    'None', deletes the key from the symbol table.
    This implementation uses a linear probing hash table. It requires that the
    key type implements the  __eq__() and __hash__() methods.
    """

    INIT_CAPACITY = 10

    def __init__(self):
        self.m = 10                     # table size
        self.n = 0                      # number of elements
        self.keys = [None] * self.m     # keys with m capacity
        self.values = [None] * self.m   # values with m capacity

    def size(self):
        """Return number of elements stored in this Symbol table."""
        return self.n

    def is_empty(self):
        """Check whether this Symbol Table is empty or not"""
        return self.n == 0

    def get(self, key):
        """Return the value associate with the given key

        Args:
            key: The key to be gotten from this collection.
        
        Returns:
            value associated with the given key if the key is in the table and
            None if the key is not in the table.
        """
        if key is None:
            raise ValueError("Can't search 'None' in the ST")
        i = self.hash(key)
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i + 1) % self.m
        if self.keys[i] is None:
            return None
        return self.values[i]

    def contains(self, key):
        """Check whether this Symbol Table contains the given key or not

        Args:
            key: The key to check if it is in the table
        
        Returns:
            True if the table contains the given key or False otherwise
        """
        if key is None:
            raise ValueError("Can't search 'None'")
        return self.get(key) is not None

    def _resize(self, capacity):
        temp = LinearProbingHashST()
        temp.m = capacity
        temp.keys = [None] * temp.m
        temp.values = [None] * temp.m

        for i in range(self.m):
            if self.keys[i] is not None:
                temp.put(self.keys[i], self.values[i])

        self.m = temp.m
        self.keys = temp.keys
        self.values = temp.values

    def hash(self, key):
        h = (abs(hash(key)) & 0x7FFFFFFF) % self.m
        return h

    def put(self, key, value):
        """Inserts the key-value pair into the symbol table.

        It overwrites the old value with the new value if the key is already
        in the symbol table. If the value is 'None', this effectively deletes the
        key from the table.
        
        Args:
            key  : The key given as string.
            value: Value associated with the given key
        """
        if key is None:
            raise ValueError("Cannot insert 'None' into the table")
        if value is None:
            self.delete(key)
            return

        if self.n * 2 == self.m:
            self._resize(2 * self.m)

        i = self.hash(key)
        while self.keys[i] is not None and key != self.keys[i]:
            i = (i + 1) % self.m

        if key == self.keys[i]:
            self.values[i] = value
            return

        self.n += 1
        self.keys[i] = key
        self.values[i] = value

    def delete(self, key):
        """Removex the given key if it is in the symbol table.

        Args:
            key: The key to be removed.
        """
        if key is None:
            raise ValueError("Cant' detele 'None' from the ST")

        if not self.contains(key):
            return

        i = self.hash(key)
        while key != self.keys[i]:
            i = (i + 1) % self.m

        self.keys[i] = None
        self.values[i] = None
        self.n -= 1

        i = (i + 1) % self.m
        while self.keys[i] is not None:
            reinserting_key = self.keys[i]
            reinserting_value = self.values[i]
            self.keys[i] = None
            self.values[i] = None
            self.n -= 1
            self.put(reinserting_key, reinserting_value)
            i = (i + 1) % self.m

        if self.n > 0 and self.n * 8 <= self.m:
            self._resize(self.m // 2)

    def keys_set(self):
        """It collects and return all the keys in the symbol table.

        Returns:
            Iterable containing all the keys in the table.
        """
        queue = []
        for key in self:
            if key is not None:
                queue.append(key)
        # for key in self.keys:
        #     if (key is not None): queue.append(key)
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
        for key in self.keys:
            if key is not None:
                yield key

    # ********************* End of Python Special Methods *********************#
