import bisect
import math
import collections
import operator
import itertools
from random import randrange, randint, choice
from collections import namedtuple
from typing import Union, List
from functools import reduce
import sys
sys.path.insert(0, '../Util')  # add Util package at begining of python path.


"""Search a sorted array for first occurrence of k. [EPI: 1]."""


def search_first_of_k(A, k):
    low, high, result = 0, len(A) - 1, -1
    # A[low:high + 1] is the candidate set.
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < k:
            low = mid + 1
        elif A[mid] > k:
            high = mid - 1
        else:
            result = mid
            high = mid - 1  # Nothing to the high of mid can be solution.
    return result
# Pythonic solution


def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


"""Search a sorted array for entry equal to its index. [EPI: 2]. """


def search_entry_equal_to_its_index(A):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < mid:
            left = mid + 1
        if A[mid] > mid:
            right = mid - 1
        else:  # A[mid] = mid
            return mid
    return -1


"""Magic Index — Find index of a SORTED array of REPEATABLE integer such that
   A[i] = i. [CtCI: 9.3] EX: [1, 1, 2, 2, 3, 3] ==> 2. """
"""Magic Index — Find index of a SORTED array of DISTINCT integer such
   that A[i] = i. [CtCI: 9.3]. """
"""Find the position of the SMALLEST element in a CYCLICALLY SORTED array of
   DISTINCT elements. Ex: [20, 30, 0, 1, 2, 3, 4] ==>> 2. [EPI: 11.3]."""


def search_smallest(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid + 1:right + 1].
            left = mid + 1
        else:  # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
            right = mid
    # Loop ends when left == right.

    return left


"""Given a sorted array of n integers that has been rotated an unknown number
   of times, write code to find an element in the array. You may assume that
   the array was originally sorted in increasing order. [CtCI: 11.3] """


def search_roated_sorted(a: list, k: int, low: int, high: int) -> None:
    if not a or low > high:
        return -1
    mid = (high + low) // 2
    if k == a[mid]:
        return mid
    if a[mid] < a[high] and a[mid] < k <= a[high]:
        return search_roated_sorted(a, k, mid+1, high)
    if a[mid] > a[high] and a[low] <= k < a[mid]:
        return search_roated_sorted(a, k, low, mid-1)
    else:  # a[mid] == a[high] or a[mid] < k <= a[high] or a[low] <= k < a[mid]
        res = search_roated_sorted(a, k, low, mid-1)
        if res == -1:
            res = search_roated_sorted(a, k, mid+1, high)
        return res


def reverse(A: list, low: int, high: int):
    while low < high:
        A[low], A[high-1] = A[high-1], A[low]
        low += 1
        high -= 1


def rotate(A: list, rotate_amount: int):
    if len(A) != 0:
        rotate_amount %= len(A)
    reverse(A, 0, len(A))
    reverse(A, 0, rotate_amount)
    reverse(A, rotate_amount, len(A))


def test_search_rotated_sorted():
    N = randint(0, 10)
    L = sorted([randint(0, 10) for _ in range(N)])
    print(L)
    rotate_amount = randint(-N, N)
    rotate(L, rotate_amount)
    print(rotate_amount, "\n", L)
    key = choice(L) if L else None
    # key = randint(-10, 10)
    res = search_roated_sorted(L, key, 0, len(L)-1)
    print("Index:", res, "key:", key)
    if res != -1:
        assert key == L[res]


"""Given a sorted array of strings which is interspersed with empty strings,
   write a method to find the location of a given string. [CtCI: 11.5] """


def search_sorted_with_empty_string(A: list, k: str):
    pass


"""Compute the integer square root. [EPI: 4]."""


def square_root(k):
    left, right = 0, k
    # Candidate interval [left, right] where everything before left has square
    # <= k, everything after right has square > k.
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


"""Compute the real square root. [EPI: 5]."""


def square_root(x):
    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)
    # Keeps searching as long as left != right.
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left


"""Find the root of a given function  using Successive Approximation
   (Newton's Method). [MIT6.00SC: PS2] """


def evaluate_poly(poly: list, x: Union[int, float]) -> float:
    """Computes the value of the polynomial (poly) function at given value x.
    Args:
        poly:    list of numbers, (len(poly) > 0).
        x:       number
Returns:
        f(x): the value of the specified polynomial at x.
    """
    f_of_x = 0.0  # --> f(x), the value of 'poly' at x.
    for i in range(len(poly)):
        f_of_x += poly[i] * (x ** i)
    return f_of_x


def compute_deriv(poly) -> List[Union[int, float]]:
    """Computes and returns the derivative of a polynomial function. If the
       derivative is 0, returns [0.0].
Args:
        poly: list of numbers, (len(poly) > 0).
    """
    f_prime_of_x = []
    if len(poly) < 2:
        return [0.0]
    for j in range(1, len(poly)):
        f_prime_of_x.append(float(j * poly[j]))
    return f_prime_of_x


def compute_root(poly: list, x_0: float, epsilon: float) -> list:
    """Uses Newton's method to find and return a root of a polynomial function.
       Returns a list containing the root and the number of iterations required
       to get to the root.
    Args:
        poly: list of numbers, (len(poly) > 1). Represents a polynomialfunction
            containing at least one real root. The derivative of this polynomial
            function at x_0 is not 0.
        x_0: initial guss.
        epsilon: ecceptable erros.
    """
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_deriv(poly), root))
        counter += 1
    return root


def _test_compute_root():
    def random_polynomial(degree):
        poly = [None]*(degree+1)
        for i in range(degree+1):
            coefficient = randint(0, 6)
            poly[i] = coefficient
        return poly
    N = randint(1, 4)
    P = random_polynomial(N)
    print(P)
    p = [5, 2]              # --> f(x) = 5x^0 + 2x^1 = 2x + 5
    rt = compute_root(p, 10, 0.0001)
    print('Root of f(x): ', rt)


"""Search in a 2D sorted array. [EPI: 6]."""


def matrix_search(A, x):
    row, col = 0, len(A[0]) - 1  # Start from the top-right corner.
    # Keeps searching while there are unclassified rows and columns.
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1  # Eliminate this row.
        else:  # A[row][col] > x.
            col -= 1  # Eliminate this column.

    return False


"""Find the min and max simultaneously. [EPI: 7]."""


def find_min_max(A, MinMax):
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)
    if len(A) <= 1:
        return MinMax(A[0], A[0])
    global_min_max = min_max(A[0], A[1])
    # Process two elements at a time.
    for i in range(2, len(A) - 1, 2):
        local_min_max = min_max(A[i], A[i + 1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest))
    # If there is odd number of elements in the array, we still need to
    # compare the last element with the existing answer.
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1]))
    return global_min_max


def _test_find_min_max():
    A = []
    MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
    find_min_max(A, MinMax)


"""Find the kth largest element. [EPI: 8]."""
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.


def find_kth_largest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx
        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
        raise IndexError('no k-th node in array A')
    return find_kth(operator.gt)
# The numbering starts from one, i.e., if A = [3, 1, -1, 2] then
# find_kth_smallest(1, A) returns -1, find_kth_smallest(2, A) returns 1,
# find_kth_smallest(3, A) returns 2, and find_kth_smallest(4, A) returns 3.


def find_kth_smallest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]

            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1

            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
        raise IndexError('no k-th node in array A')
    return find_kth(operator.lt)


"""Find the missing IP address. [EPI: 9]."""


def find_missing_element(stream):
    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1
    # Look for a bucket that contains less than (1 << 16) elements.
    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(
        i for i, c in enumerate(counter) if c < BUCKET_CAPACITY)
    # Finds all IP addresses in the stream whose first 16 bits are equal to
    # candidate_bucket.
    candidates = [0] * BUCKET_CAPACITY
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # Records the presence of 16 LSB of x.
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1
    # At least one of the LSB combinations is absent, find it.
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i
    raise ValueError('no missing element')


"""Find the duplicate and missing elements. [EPI: 10]."""


def find_duplicate_missing(A, DuplicateAndMissing):
    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A.
    miss_XOR_dup = reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)
    # We need to find a bit that's set to 1 in miss_XOR_dup. Such a bit must
    # exist if there is a single missing number and a single duplicated number
    # in A.
    #
    # The bit-fiddling assignment below sets all of bits in differ_bit
    # to 0 except for the least significant bit in miss_XOR_dup that's 1.
    differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
    for i, a in enumerate(A):
        # Focus on entries and numbers in which the differ_bit-th bit is 1.
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a
    # miss_or_dup is either the missing value or the duplicated entry.
    # If miss_or_dup is in A, miss_or_dup is the duplicate;
    # otherwise, miss_or_dup is the missing value.
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup)
            if miss_or_dup in A else DuplicateAndMissing(
                miss_or_dup ^ miss_XOR_dup, miss_or_dup))


def _test_find_duplicate_missing():
    A = []
    DupAndMissing = namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))
    find_duplicate_missing(A, DupAndMissing)


if __name__ == "__main__":
    # _test_compute_root()
    test_search_rotated_sorted()
    pass
