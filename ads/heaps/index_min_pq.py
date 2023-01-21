"""
Implementation of a indexed min priority queue of generic keys.
"""
from typing import List, TypeVar, Generic

T = TypeVar('T')


class IndexMinPQ(Generic[T]):
    """Implementation of a indexed min priority queue of generic keys.

    This class provides basic functionality of a indexed min priority queue of
    generic key which uses a binary heap abstraction. In order to let the
    client refer to keys on the priority queue, an integer between 0 and
    'maxN - 1' is associated with each key — the client uses this integer to
    specify which key to delete or change.
    """
    def __init__(self, maxN):
        self.maxN: int = maxN  # maximum number of elements on PQ
        self.pq: List = [-1] * (self.maxN + 1)  # PQ using 1-based indexing
        # key-index, qp[pq[i]] = pq[qp[i]] = i
        self.qp: List = [-1] * (self.maxN + 1)
        self.keys: T = [None] * (self.maxN + 1)  # keys[i] = priority of i
        self.n: int = 0  # Number of elements on the queue

    def size(self):
        """Return the number of keys in this queue."""
        return self.n

    def is_empty(self):
        """ Check whether this Queue is empty or not."""
        return self.n == 0

    def contains(self, i):
        """ Check if i is an index on this priority queue.

        Args:
            i : the index of a key
        Returns:
            true if i is an index on this priority queue; false otherwise.
        """
        if (i < 0 or i >= self.maxN):
            raise ValueError("index out of bound")
        return self.qp[i] != -1

    def add(self, i, key):
        """Adds the given key to this queue

        Args:
            i   : Index of the key to be added.
            key : The key to be added to the queue.
        """
        if key is None:
            raise ValueError("key can't be 'None'")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self._swim(self.n)

    def delete_min(self):
        """Removes and returns the smallest key from this queue.
        """
        if self.is_empty():
            raise RuntimeError("PQ Underflowed")
        min = self.pq[1]
        self._swap(1, self.n)
        self.n -= 1
        self._sink(1)
        # assert min == self.pq[self.n + 1]
        self.pq[self.n + 1] = -1
        self.qp[min] = -1
        self.keys[min] = None
        # assert self.is_min_heap()
        return min

    def min_key(self):
        """Returns the smallest key from this queue without removing it.
        """
        if self.is_empty():
            raise RuntimeError("PQ Underflowed")
        return self.keys[self.pq[1]]

    def min_index(self):
        """ Return the index associated with minimum key.
        """
        if self.is_empty():
            raise RuntimeError("PQ Underflowed")
        return self.pq[1]

    def key_of(self, i):
        """ Return the key associated with the given index, i.

        Args:
            i : the index of which key is to be returned
        """
        if i < 0 and i >= self.maxN:
            raise IndexError("Index out of range")
        if not self.contains(i):
            raise IndexError("PQ Underflowed")
        return self.keys[i]

    def change_key(self, i, key):
        """Change the key associated with given index (i) to the given key.

        Args:
            i   : the index whose key is to be changed.
            key : the key which is to be associated with given index (i).
        """
        if i < 0 and i >= self.maxN:
            raise IndexError("Index out of range")
        if not self.contains(i):
            raise IndexError("PQ Underflowed")
        self.keys[i] = key
        self._sink(self.qp[i])
        self._swim(self.qp[i])

    def decrease_key(self, i, key):
        """Decrease the key associated with index i to the given key.

        Args:
            i   : the index whose key to be decreased.
            key : the new decreased key to be associated with given index (i).
        """
        if (i < 0 and i >= self.maxN):
            raise IndexError("Index out of range")
        if not self.contains(i):
            raise KeyError("key not in this queue")
        if self.keys[i] <= key:
            raise ValueError("The given key isn't decrease-able")
        self.keys[i] = key
        self._swim(self.qp[i])

    def increase_key(self, i, key):
        """ Increase the key associated with index i to the given key.

        Args:
            i   : the index whose key to be increased.
            key : the new increased key to be associated with given index (i).
        """
        if (i < 0 and i >= self.maxN):
            raise IndexError("Index out of range")
        if not self.contains(i):
            raise KeyError("key not in this queue")
        if self.keys[i] >= key:
            raise ValueError("The given key isn't decrease-able")
        self.keys[i] = key
        self._sink(self.qp[i])

    def delete(self, i):
        """ Delete the key associated with the given index, i.

        Args:
            i : the index of key to be deleted.
        """
        if (i < 0 and i >= self.maxN):
            raise IndexError("Index out of range")
        if not self.contains(i):
            raise KeyError("key not in this queue")
        index = self.qp[i]
        self._swap(index, self.n)
        self.n -= 1
        self.keys[i] = None
        self._swim(index)
        self._sink(index)
        self.qp[i] = -1
        self.pq[self.n + 1] = -1

    def keys_inorder(self):
        """ Return the keys of this PQ following in-order traversal.

        Returns:
            (iterable): An iterable containing all the keys of this priority queue.
        """
        keys = []
        q = self._copy()
        for i in range(q.n):
            keys.append(q.delete_min())
        return keys

    def _copy(self):
        q = IndexMinPQ(self.maxN)
        for i in range(1, self.n + 1):
            q.add(self.pq[i], self.keys[self.pq[i]])
        return q

    def _swim(self, k):
        """Percolate the element at given index up.

        Args:
            k : The index of a element into the priority queue.
        """
        while (k > 1 and self._greater(k // 2, k)):
            self._swap(k // 2, k)
            k = k // 2

    def _sink(self, k):
        """Percolate the element at given index down.

        Args:
            k : The index of a element into the priority queue.
        """
        while (2 * k <= self.n):
            j = 2 * k
            if j < self.n and self._greater(j, j + 1):
                j += 1
            if not self._greater(k, j):
                break
            self._swap(j, k)
            k = j

    def _smaller(self, i, j):
        """Compare the order of the keys at the given indices

        Args:
            i : The index of the key to be compared.
            j : The index of the key to be compared.
        """
        return self.keys[self.pq[i]] < self.keys[self.pq[j]]

    def _greater(self, i, j):
        """Compare the order of the keys at the given indices

        Args:
            i : The index of the key to be compared.
            j : The index of the key to be compared.
        """
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def _swap(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def __len__(self):
        return self.size()

    def __delitem__(self, key):
        self.delete_min()

    def __iter__(self):
        q = self._copy()
        for i in range(q.n):
            yield q.delete_min()
