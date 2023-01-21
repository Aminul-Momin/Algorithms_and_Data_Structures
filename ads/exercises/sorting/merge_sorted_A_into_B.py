from random import randrange

from ads.utils import is_sorted
#==============================================================================
"""
You are given two sorted arrays, A and B, where A has a large enough
buffer at the end to hold B. Write a method to merge B into A in sorted
order - [EPI:13.2, CtCI: 11.1].
"""


def merge_two_sorted_arrays(A, m, B, n):

    a, b, write_idx = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1


def main():
    r1 = randrange(10)
    r2 = randrange(r1, 20)
    L1 = sorted([randrange(-5, 6) for _ in range(r1)])
    L2 = sorted([randrange(-5, 6) for _ in range(r2)])

    L1 = L1 + [None] * (len(L2))
    merge_two_sorted_arrays(L1, r1, L2, r2)


if __name__ == '__main__':
    main()
