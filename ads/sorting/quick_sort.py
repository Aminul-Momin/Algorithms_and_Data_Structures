from ..utils.utils import *
#==============================================================================
""" Implementation of quick sort algorithm.

This modules provides two functions for sorting a list using quicksort
algorithm.
"""


def quick_sort(a):
    """Sorts given list using Quicksort algorithm.

    Args:
        a (list): The list to be sorted
    """
    def _quick_sort(a, low, high):
        if low >= high:
            return
        pivot_idx = partition(a, low, high)
        _quick_sort(a, low, pivot_idx - 1)
        _quick_sort(a, pivot_idx + 1, high)

    def partition(a, low, high):
        """partition the subarray a[low, ..., high].

        Partitions the subarray a[low, ..., high] so that a[low..j-1]
        <= a[j] <= a[j+1..high] and return the index j.

        Args:
            a   : the array to be partioned.
            low : the lower index into the specified array.
            high: the upper index into the specified array.
        """
        pivot, idx = a[high], low

        for i in range(low, high):
            if a[i] < pivot:
                swap(a, idx, i)
                idx = idx + 1

        swap(a, idx, high)
        return idx

    # called the quicksort procedure
    _quick_sort(a, 0, len(a) - 1)


def quick_sort_v2(a):
    """Sorts given list using Quicksort algorithm.

    Args:
        a (list): The list to be sorted
    """
    def _quick_sort_v2(a, low, high):
        if low >= high:
            return
        pi = partition_v2(a, low, high)  # pi -> Pivot Index
        _quick_sort_v2(a, low, pi - 1)
        _quick_sort_v2(a, pi + 1, high)

    def partition_v2(a, low, high):
        """partition the subarray a[low, ..., high].

        Partitions the subarray a[low, ..., high] so that a[low..j-1]
        <= a[j] <= a[j+1..high] and return the index j.

        Args:
            a   : the array to be partioned.
            low : the lower index into the specified array.
            high: the upper index into the specified array.
        """

        pivot, i, j = a[low], low + 1, high
        while True:
            while a[i] < pivot:  # find item on low to swap
                if i == high:
                    break
                i += 1

            while a[j] >= pivot:  # find item on high to swap
                if j == low:
                    break  # redundant since a[low] acts as sentinel
                j -= 1

            if i >= j:
                break  # check if pointers cross

            swap(a, i, j)

        swap(a, low, j)  # put partitioning item pivot at a[j]

        # now, a[low ... j-1] <= a[j] <= a[j+1 ... high]
        return j

    # called the quicksort procedure
    _quick_sort_v2(a, 0, len(a) - 1)


def quick_sort_v3(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_v3(left) + middle + quick_sort_v3(right)


def _main():
    for _ in range(1000):
        for sort in [quick_sort, quick_sort_v2, quick_sort_v3]:
            P = [randrange(1, 150) for _ in range(randrange(1, 15))]
            try:
                returned = sort(P)
                expected = sorted(P)
                
                if sort.__name__ == 'quick_sort_v3':
                    assert returned == expected
                else:
                    #print(sort.__name__)
                    assert P == expected
            except AssertionError:
                print(f"FunctionName:\t{sort.__name__} ==> {red('AssertionError')}")
                print(P, returned, expected)
                break

# ================================================================


if __name__ == '__main__':
    _main()
