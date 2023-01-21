from ads.utils import swap, is_sorted
from random import randrange
"""Implementation of Insertion Sort."""


def insertion_sort(L):
    """Sorts the given list using insertion sort algorithm.

    Args:
        a (list): The list to be sorted
    """
    for i in range(len(L)):
        idx = i
        while idx > 0 and L[idx - 1] > L[idx]:
            swap(L, idx, idx - 1)
            idx -= 1


def main():
    L = [randrange(-99, 100) for _ in range(10)]
    assert not is_sorted(L)
    sorted_L = sorted(L)
    insertion_sort(L)
    assert L == sorted_L


if __name__ == '__main__':
    main()
