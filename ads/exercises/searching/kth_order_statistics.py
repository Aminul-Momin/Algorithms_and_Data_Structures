import operator
from time import sleep, time
from random import randint, sample
from ads.utils import swap
#==============================================================================
""" Find the kth smallest element from a distinct elements of list. - [EPI: 11.8]

    Examples:
        1. find_kth_smallest(1, [3, 1, -1, 2])  -> -1
        2. find_kth_smallest(2, [3, 1, -1, 2])  ->  1
        3. find_kth_smallest(3, [3, 1, -1, 2])  ->  2
        4. find_kth_smallest(4, [3, 1, -1, 2])  ->  3
"""


def find_kth_smallest(k, A):
    def find_kth(comp):
        """Partition A[low:high + 1] around pivot_idx.
        
        After partitioning, A[low:new_pivot_idx] contains elements that are
        "less than" the pivot, and A[new_pivot_idx + 1:high + 1] contains
        elements that are "greater than" the pivot.
        """
        def partition_around_pivot(low, high, pivot_idx):
            """Returns the new index of the pivot element after partition."""
            pivot_value = A[pivot_idx]
            new_pivot_idx = low
            swap(A, pivot_idx, high)

            for i in range(low, high):
                if comp(A[i], pivot_value):
                    swap(A, new_pivot_idx, i)
                    new_pivot_idx += 1

            swap(A, new_pivot_idx, high)
            return new_pivot_idx

        low, high = 0, len(A) - 1
        while low <= high:
            # Generates a random integer in [low, high].
            pivot_idx = randint(low, high)
            ith_smallest = partition_around_pivot(low, high, pivot_idx)

            if ith_smallest + 1 < k: low = ith_smallest + 1
            elif ith_smallest + 1 > k: high = ith_smallest - 1
            else: return A[ith_smallest]

    return find_kth(operator.lt)


def main():
    L = sample([*range(500)], 100)
    k = randint(1, len(L))
    expected = sorted(L)[k - 1]
    returned = find_kth_smallest(k, L)
    # print(k, expected, returned, L)
    assert expected == returned


if __name__ == '__main__':
    main()
