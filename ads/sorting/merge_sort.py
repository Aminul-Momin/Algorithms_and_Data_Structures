from typing import List
import time
from random import randint

from ads.utils.utils import *
"""Implementation of merge sort algorithm.

This modules provides several functions, implemented in various ways, for
sorting a list using mergesort algorithm.
"""


def merge_sort(L: List) -> List:
    """Sorts and returns the specified list using merge-sort algorithm.

    Args:
        L: the list to be sorted
    Returns:
        a sorted list containing all elements of the given list, L
    """
    def merge(L1: List, L2: List) -> List:
        """It returns a sorted list after stably merging L1 with L2.

        Args:
            L1: sorted list to be merged with L2 into a new list
            L2: sorted list to be merged with L1 into a new list
        Returns:
            a sorted list containing all elements of both list - L1 and L2.
        """
        L = L1 + L2
        left_index, right_index = 0, 0

        for i in range(len(L)):
            if left_index >= len(L1):
                L[i] = L2[right_index]
                right_index += 1
            elif right_index >= len(L2):
                L[i] = L1[left_index]
                left_index += 1
            elif L2[right_index] < L1[left_index]:  # ensure stability
                L[i] = L2[right_index]
                right_index += 1
            else:
                L[i] = L1[left_index]
                left_index += 1
        return L

    N = len(L)
    if N <= 1: return L

    mid = N // 2
    left = merge_sort(L[0:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)


# ************************ Alternative implementations ************************#
def merge_sort_v2(a: List) -> None:
    """Sorts the  specified list using merge-sort algorithm.

    Args:
        a: the list to be sorted
    """
    def _merge_sort_v2(a: List, low: int, high: int) -> None:
        """It sorts a[low ... high] by first deviding it into a[low ... mid] and
        a[mid+1 ... high] and then merging them

        Args:
            a   : the array to be sorted
            low : first index of first half of the array, a[low ... mid]
            high: last index of second half of the array, a[mid+1 ... high]
        """
        if low >= high: return
        mid = (low + high) // 2

        # sorts first half of the array, a[low ... mid]
        _merge_sort_v2(a, low, mid)

        # sorts first half of the array, a[mid+1 ... high]
        _merge_sort_v2(a, mid + 1, high)

        # merges a[low ... mid] and a[mid+1 ... high], two halves of the array
        merge_v2(a, low, mid, high)

    _merge_sort_v2(a, 0, len(a) - 1)


def merge_v2(a: List, low: int, mid: int, high: int):
    """It stably merges a[low ... mid] with a[mid+1 ... high] using an
    auxilary array, aux[low ... high]

    Args:
        a   : the array is being sorted
        low : initial index of first half of the array, a[low ... mid]
        mid : last index of first half of the array, a[low ... mid]
        high: last index of second half of the array, a[mid+1 ... high]
    """

    aux = [item for item in a]
    left, right, i = low, mid + 1, low

    while left <= mid and right <= high:
        if aux[left] <= aux[right]:  # ensures stability
            a[i] = aux[left]
            left += 1
            i += 1
        else:
            a[i] = aux[right]
            right += 1
            i += 1

    while left <= mid:
        a[i] = aux[left]
        i += 1
        left += 1


# ************************ Alternative implementations ************************#


def merge_sort_v3(a: List):
    """Sorts the  specified list using merge-sort algorithm.

    Args:
        a: the list to be sorted
    """
    def _merge_sort_v3(a: List, low: int, high: int, aux: List) -> None:
        """It sorts a[low ... high] by first deviding it into a[low ... mid] and
        a[mid+1 ... high] and then merging them

        Args:
            a   : the array to be sorted
            low : first index of first half of the array, a[low ... mid]
            high: last index of second half of the array, a[mid+1 ... high]
            aux : the auxilary array for recycling
        """
        if low >= high: return
        mid = (low + high) // 2

        # sorts first half of the array, a[low ... mid]
        _merge_sort_v3(a, low, mid, aux)

        # sorts first half of the array, a[mid+1 ... high]
        _merge_sort_v3(a, mid + 1, high, aux)

        # merges a[low ... mid] and a[mid+1 ... high], two halves of a[low...high]
        merge_v3(a, low, mid, high, aux)

    aux = [None] * len(a)
    _merge_sort_v3(a, 0, len(a) - 1, aux)


def merge_v3(a: List, low: int, mid: int, high: int, aux: List) -> None:
    """It stably merges a[low ... mid] with a[mid+1 ... high] using an
    auxilary array, aux[low ... high]

    Args:
        a   : the array is being sorted
        low : first index of first half of the array, a[low ... mid]
        mid : last index of first half of the array, a[low ... mid]
        high: last index of second half of the array, a[mid+1 ... high]
        aux : the auxilary array for recycling
    """
    for i in range(low, high + 1):
        aux[i] = a[i]

    left_index, right_index = low, mid + 1

    for i in range(low, high + 1):
        if left_index > mid:
            a[i] = aux[right_index]
            left_index += 1
        elif right_index > high:
            a[i] = aux[left_index]
            right_index += 1
        elif aux[right_index] < aux[left_index]:  # ensures stability
            a[i] = aux[right_index]
            right_index += 1
        else:
            a[i] = aux[left_index]
            left_index += 1


def _main():
    for _ in range(1000):
        P = [randrange(1, 150) for _ in range(randrange(1, 15))]
        try:
            returned1 = merge_sort(P)
            returned2 = merge_sort_v2(P)
            expected = sorted(P)
            assert returned2 == expected
        except AssertionError:
            print(red('FAILED'))
            print(P, returned1, returned2, expected)

# ================================================================


if __name__ == '__main__':
    _main()
