from typing import Sequence

""" Find element from a sorted and rotated array. - [CtCI: 11.3].

    Given a sorted array of n integers that has been rotated an unknown number
    of times, write code to find an element in the array. You may assume that
    the array was originally sorted in increasing order.

    Examples:
        1. search_rotated_sorted([], 2)  -> -1
        2. search_rotated_sorted([4,4,1,2,4], 2)  ->  3
        3. search_rotated_sorted([5,6,7,8,1], 6)  ->  1
        4. search_rotated_sorted([4,4,4,4,6,4], 6)  ->  4
        5. search_rotated_sorted([0,1,4,4,4,4], 1)  ->  1
        6. search_rotated_sorted([1,4,4,4], -1)  -> -1
        7. search_rotated_sorted([8,0,1,2,8], 0)  ->  1
        8. search_rotated_sorted([9, 2, 9, 9, 9], 2)  ->  1
        9. search_rotated_sorted([9, 9, 9, 2, 9], 2)  ->  3
"""


def find_rotated_sorted_rec(L: Sequence[int], key: int) -> int:
    """Find an element from a rotated and sorted array in ascending order.

    Args:
        a  : The sorted list to search into.
        key: The element to be found from the given list.

    Returns:
        The index of the element if found else -1.
    """
    return rotated_sorted_rec(L, key, 0, len(L) - 1)



def rotated_sorted_rec(a, k, low, high):
    if not a or low > high:
        return -1

    mid = (low + high) // 2
    if a[mid] == k:
        return mid

    if a[low] < a[mid]:  # left side normally sorted
        if a[low] <= k < a[mid]:
            return rotated_sorted_rec(a, k, low, mid - 1)
        else:
            return rotated_sorted_rec(a, k, mid + 1, high)
    elif a[low] > a[mid]:  # right side is normally sorted
        if a[mid] < k <= a[high]:
            return rotated_sorted_rec(a, k, mid + 1, high)
        else:
            return rotated_sorted_rec(a, k, low, mid - 1)
    else:  # a[low] == a[mid] -> Left or right half is all repeats
        if a[mid] != a[high]:
            return rotated_sorted_rec(a, k, mid + 1, high)
        else:  # unknown which side is normally sorted
            left = rotated_sorted_rec(a, k, low + 1, mid - 1)
            if left != -1:
                return left
            else:
                return rotated_sorted_rec(a, k, mid + 1, high - 1)
