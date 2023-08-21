from typing import Container
#==============================================================================
""" Search a sorted array for entry equal to its index. - [EPI:11.2,CtCI:9.3].

    Write a function 'magic_index(L)' that takes as input a SORTED array of
    DISTINCT integer and returns the index 'i' in L such that L[i] == i.

     Examples:
        1. magic_index([])              -> -1
        2. magic_index([0, 1, 2, 3])    ->  1
        3. magic_index([-1, 0, 1, 3])   ->  3
        4. magic_index([0, 1, 2, 3])    ->  1
        5. magic_index([0,2,3])         ->  0
"""


def magic_index(L: Container[int]) -> int:
    """Finds the index in 'L' where L[index] == index.
    Args:
        L: A SORTED array of DISTINCT integer.

    Returns:
        The index in 'L' where L[index] == index.
    """

    left, right = 0, len(L) - 1

    while left <= right:

        mid = (left + right) // 2

        if L[mid] < mid: left = mid + 1
        elif L[mid] > mid: right = mid - 1
        else: return mid  # L[mid] == mid

    return -1


""" Search a sorted array for entry equal to its index. - [EPI: 11.2, tCI: 9.3].

    Write a function 'magic_index_v2(L)' that takes as input a SORTED array
    of REPEATABLE integer and returns the index 'i' in L such that L[i] == i.

     Examples:
        1. magic_index_v2([0,0,2,2])       ->  0
        2. magic_index_v2([0,1,1,2,3])     ->  0
        3. magic_index_v2([3,3,3,3])       ->  3
        4. magic_index_v2([])              -> -1
        5. magic_index_v2([0, 1, 2, 3])    ->  1
        6. magic_index_v2([-1, 0, 1, 3])   ->  3
        7. magic_index_v2([0, 1, 2, 3])    ->  1
        8. magic_index_v2([0,2,3])         ->  0
"""


def magic_index_v2(L: Container[int]) -> int:
    """Finds the index in 'L' where L[index] == index.

    Args:
        L: A SORTED array of REPEATABLE integer.

    Returns:
        The index in 'L' where L[index] == index.
    """
    def magic_idx_v2(L, low, high):
        if not L: return -1
        if low > high: return -1

        mid = (low + high) // 2

        if L[mid] == mid: return mid
        else:
            left = magic_idx_v2(L, low, min(L[mid], mid - 1))
            if left != -1: return left
            else: return magic_idx_v2(L, max(L[mid], mid + 1), high)

    return magic_idx_v2(L, 0, len(L) - 1)
