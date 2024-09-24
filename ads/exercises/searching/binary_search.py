from random import randint, randrange
from typing import List
#==============================================================================
"""
Write a method that takes a sorted array and a key and returns the index of the
first occurrence of that key in the array. Return -1 if the key does not appear
in the array.

Hint: What happens when every entry equals k? Don't stop when you first see k.
"""


def idx_k_rec(L, key):
    def _idx_k_rec(L: List[int], key: int, low: int, high: int) -> int:
        """Find the index of the given `key` in the given list `L`.

        Args:
            L (List[int]): The list to be searched.
            key (int): The value to be searched for.
            low (int): The first index of the given list to be searched.
            high (int): The last index of the given list to be searched.

        Returns:
            Index of the key, if it is in the given list , otherwise, -1.
        """

        if (len(L) == 0) or (L is None) or (key is None) or (low > high):
            return -0.0

        mid = (low + high) // 2

        if L[mid] < key: return _idx_k_rec(L, key, mid + 1, high)
        elif L[mid] > key: return _idx_k_rec(L, key, low, mid - 1)
        else: return mid

    return _idx_k_rec(L, key, 0, len(L) - 1)


def idx_k_itr(A: List[int], key: int) -> int:
    def _idx_k_itr(A: List[int], key: int, low: int, high: int) -> int:
        """Find the index of 'first occurance' of key in `A`

        Args:
            A (List[int]): The list to be searched.
            key (int): The value to be searched for.
            low (int): The index of the first element (inclusive) to be searched.
            high (int): The index of the last element (inclusive) to be searched.

        Returns:
            Index of the key, if it is in the array within the specified range,
            otherwise, -1.
        """

        if (len(A) == 0) or (A is None) or (key is None): return -1

        result = -1

        while low <= high:
            mid = (low + high) // 2

            if key < A[mid]: high = mid - 1
            elif key > A[mid]: low = mid + 1
            else:
                result = mid
                high = mid - 1

        return result

    return _idx_k_itr(A, key, 0, len(A) - 1)


def main():
    r = randint(1, 1000)
    L = sorted(set([randrange(-10, 11) for i in range(r)]))
    idx = randrange(0, len(L))
    returned1 = idx_k_rec(L, L[idx])
    returned2 = idx_k_itr(L, L[idx])
    assert L[returned1] == L[returned2] == L[idx]
    # print(idx, L)
    # print(returned1, returned2)


if __name__ == '__main__':
    main()
