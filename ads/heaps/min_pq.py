"""
This module contains implementation of a min priority queue of generic keys.
"""

from typing import TypeVar, Iterable

K = TypeVar('K')


class MinPQ:
    """Implementation of a min priority queue of generic keys.

    This class provides basic functionalities of a min priority queue of
    generic key which uses a binary heap abstraction. It includes a map of
    keys to their indices in the heap so that key lookup is constant time and
    decrease_key(key), increase_key(key), change_key(key) is O(log n) time.
    """
    def __init__(self):
        """Initializes the priority queue.
        """
        self._pq = [None]  # priority queue of 1-based indexing.
        self._key_index = {}  # key to index mapping.

    def size(self) -> int:
        """Return the number of keys in this queue.
        """
        return len(self._pq) - 1

    def is_empty(self) -> bool:
        """Check whether this Queue is empty or not.
        """
        return self.size() == 0

    def contains(self, key: K) -> bool:
        """Check whether this Queue contains the given key or not.

        Args:
        ----
            key: the key to be checked if it is in this queue.
        """
        return key in self._key_index

    def add(self, key: K) -> None:
        """Adds a key into the priority queue.
        
        Args:
        ----
            key: the key to be added into this queue.
        """
        self._pq.append(key)
        idx = len(self._pq)
        self._key_index[key] = idx
        self._shift_up(idx)

    def delete_min(self) -> K:
        """Removes and returns the minimum key.
        """
        if self.is_empty(): return None
        self._swap(1, len(self))
        min = self._pq.pop()
        del self._key_index[min]
        self._shift_down(1)
        return min

    def decrease_key(self, key: K) -> None:
        """Decreases the value of the key if it is in the priority queue.

        Args:
        ----
            key : the key to be deccreased.
        
        Raise:
        -----
            KeyError: if the given key not in this queue.
        """
        if not self.contains(key): raise KeyError("key not queue")
        index = self._key_index[key]
        if index: self._shift_up(index)

    def increase_key(self, key: K) -> None:
        """Increases the value of the key if it is in the priority queue.

        Args:
        ----
            key : the key to be increased.
        
        Raise:
        -----
            KeyError: if the given key not in this queue.
        """
        if not self.contains(key): raise KeyError("key not queue")
        index = self._key_index[key]
        if index: self._shift_down(index)

    def change_key(self, old_key: K, new_key: K) -> None:
        """Replace the old_key by the new_key and then reheapify this queue.

        Args:
        ----
            old_key : the key to be replaced by new key.
            new_key : the key by which old_key is to be replaced.
        
        Raise:
        -----
            KeyError: if the given old_key not in this queue.
        """
        if not self.contains(old_key): raise KeyError("key not queue")
        index = self._key_index[old_key]
        del self._key_index[old_key]
        self._pq[index] = new_key
        self._key_index[new_key] = index
        self._shift_down(index)
        self._shift_up(index)

    def delete(self, key: K) -> None:
        """Removes the given key from the priority queue.

        Args:
        ----
            key: the key to be deleted from this queue.
        
        Raise:
        -----
            KeyError: if the given key not in this queue.
        """
        if not self.contains(key): raise KeyError("key not queue")
        index = self._key_index[key]
        del self._key_index[key]
        self._swap(index, len(self._pq))
        self._pq.pop()
        self._shift_down(index)

    def min_key(self) -> K:
        """Return the smallest key from this queue without removing it.
        
        Raise:
        -----
            RuntimeError: if this queue is empty.
        """
        if self.is_empty(): raise RuntimeError("PQ Underflowed")
        return self._pq[1]

    def min_index(self) -> int:
        """Return the index associated with minimum key.
        
        Raise:
        -----
            RuntimeError: if this queue is empty.
        """
        if self.is_empty(): raise RuntimeError("PQ Underflowed")
        return self._key_index[self._pq[1]]

    def key_of(self, idx) -> K:
        """Return the key associated with the given index, idx.

        Args:
        ----
            idx : the index of which key is to be returned.
        
        Raise:
        -----
            RuntimeError: if the given index, idx, out of range.
        """
        if idx < 0 and idx > self.size():
            raise IndexError("index out of range")
        return self._pq[idx]

    def keys_inorder(self) -> Iterable[K]:
        """Return the keys of this PQ following in-order traversal.

        Returns:
        -------
            an iterable containing all the keys of this priority queue.
        """
        keys = []
        q = self._copy()
        for i in range(q.size()):
            keys.append(q.delete_min())
        return keys

    def _copy(self) -> 'MinPQ':
        q = MinPQ()
        for i in range(1, self.size() + 1):
            q.add(self._pq[i])
        return q

    #--------------------------- Helper functions: ---------------------------#

    def _shift_up(self, idx: int) -> None:
        """Percolate the element at given index up.

        Args:
        ----
            idx : the index of a element into the priority queue.
        """
        parent_idx = idx // 2
        while (idx > 1 and self._pq[parent_idx] > self.qp[idx]):
            self._swap(parent_idx, idx)
            idx = parent_idx

    def _shift_down(self, idx: int) -> None:
        """Percolate the element at given index down.

        Args:
        ----
            idx : the index of a element into the priority queue.
        """
        child_idx = 2 * idx
        while (child_idx <= self.size()):
            j = child_idx
            if j < self.size() and self._greater(j, j + 1): j += 1
            if j < self.size() and self._smaller(idx, j): break
            self._swap(j, idx)
            idx = j

    def _smaller(self, i, j):
        """Compare the order of the keys at the given indices

        Args:
        ----
            i (int) : the index of the key to be compared.
            j (int) : the index of the key to be compared.
        Returns:
        --------
            bool: True if key at 'i' is smaller than key at 'j', False otherwise.
        """
        return self._pq[i] < self._pq[j]

    def _greater(self, i, j):
        """Compare the order of the keys at the given indices

        Args:
        ----
            i (int) : the index of the key to be compared.
            j (int) : the index of the key to be compared.
        Returns:
        --------
            bool: True if key at 'i' is larger than key at 'j', False otherwise.
        """
        return self._pq[i] > self._pq[j]

    def _swap(self, i, j):
        """Swaps the key at indices i and j and updates the key to index map.
        """
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]
        self._key_index[self._pq[i]], self._key_index[self._pq[j]] = i, j

    def check_ri(self):
        pq = self._pq
        i = 1
        while i <= (len(pq) - 1) // 2:
            l = i * 2
            if pq[i] > pq[l]:
                raise ValueError('Left child is smaller than parent.')
            r = i * 2 + 1
            if r < len(pq) and pq[i] > pq[r]:
                raise ValueError('Right child is smaller than parent.')
            i += 1

        for key, index in self._key_index.items():
            if self._pq[index] is not key:
                raise ValueError('Key index mapping is wrong.')

    #************************ Python Special Methods: ************************#
    def __len__(self):
        return len(self._pq) - 1

    def __getitem__(self, i):
        return self._pq[i]

    def __setitem__(self, i, key):
        self._pq[i] = key

    #********************* End of Python Special Methods *********************#


def main():
    pass


if __name__ == '__main__':
    main()