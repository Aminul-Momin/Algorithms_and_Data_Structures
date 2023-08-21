"""
Solves questions related to searching algorithms.
"""

import bisect, math, collections, operator, itertools
from random import randint
from collections import namedtuple
from functools import reduce
from typing import Container, List, Sequence, Union

# ============================================================================
# ============================================================================

""" Search a sorted array for first occurrence of k. - [EPI: 11.1].

    Write a function 'search_first_of_k(L, key)' which takes as input a sorted
    array and a key and returns the index of the first occurance of the key in
    the array.

    Examples:
        1. search_first_of_k([], key)           -> -1.0
        2. search_first_of_k([1,2,2,2], 2)      ->  1
        3. search_first_of_k([1,2,3], 3)        ->  2
        4. search_first_of_k([1,1,1,1], key)    ->  0
"""


def search_first_of_k(L: List[Union[int, chr, str]], key: Union[int, chr,
                                                                str]):

    if (len(L) == 0) or (L is None) or (key is None): return -1.0

    low, high, result = 0, len(L) - 1, -1.0

    while low <= high:
        mid = (low + high) // 2

        if key < L[mid]: high = mid - 1
        elif key > L[mid]: low = mid + 1
        else:
            result = mid
            high = mid - 1

    return result


# NOTE: It's not returning the FIRST occurance !!
def idx_k_rec(L, k, low, high):

    if (len(L) == 0) or (L is None) or (k is None) or (low > high):
        return -0.0

    mid = (low + high) // 2

    if L[mid] < k: return idx_k_rec(L, k, mid + 1, high)
    elif L[mid] > k: return idx_k_rec(L, k, low, mid - 1)
    else: return mid


def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_low(A, k)
    return i if i < len(A) and A[i] == k else -1


def idx_k_nearest(L, k):
    pass


def idx_k_nearest_rec(L, k, low, high):
    pass


""" Search a sorted array for entry equal to its index. - [EPI: 11.2, tCI: 9.3].

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
        L: The container of the sorted integers.

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
        L: The container of the sorted integers.

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


""" Find the smallest element in a cyclically sorted array. - [EPI: 11.3].

    Write a function 'search_smallest(A)' which takes in as input a CYCLICALLY
    SORTED array of DISTINCT elements and returns the index of the smallest
    element in the array.

    NOTE:
        Order of sortedness and direction of rotation of the given array
        does not matter.

    Examples:
        1.search_smallest([6,1,2,4,5])         ->  1
        2.search_smallest([5,6,7,8,1])         ->  4
        3.search_smallest([4,3,2])             ->  2
        4.search_smallest([0,1,4])             ->  0
        6.search_smallest([9,0,1,2,8])         ->  1
"""


def search_smallest(A):

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid + 1:right + 1].
            left = mid + 1
        else:  # A[mid] <= A[right].
            # Minimum cannot be in A[mid+1:right+1] so it must be in A[left:mid+1].
            right = mid
    # Loop ends when left == right.
    return left


# NOTE: DOES NOT WORK !
def search_smallest_v2(A):

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[left] > A[mid]:
            # Minimum must be in A[left: mid+1].
            right = mid
        else:  # A[left] <= A[mid].
            # Minimum cannot be in A[] so it must be in A[left:mid + 1].
            left = mid + 1

    return left


""" Find element from a sorted and rotated array. - [CtCI: 11.3].

    Given a sorted array of n integers that has been rotated an unknown number
    of times, write code to find an element in the array. You may assume that
    the array was originally sorted in increasing order.

    Examples:
        1. search_rotated_sorted([], 2)                  -> -1
        2. search_rotated_sorted([4,4,1,2,4], 2)         ->  3
        3. search_rotated_sorted([5,6,7,8,1], 6)         ->  1
        4. search_rotated_sorted([4,4,4,4,6,4], 6)       ->  4
        5. search_rotated_sorted([0,1,4,4,4,4], 1)       ->  1
        6. search_rotated_sorted([1,4,4,4], -1)          -> -1
        7. search_rotated_sorted([8,0,1,2,8], 0)         ->  1
        8. search_rotated_sorted([9, 2, 9, 9, 9], 2)     ->  1
        9. search_rotated_sorted([9, 9, 9, 2, 9], 2)     ->  3
"""


def find_rotated_sorted_rec(L: Sequence[int], key: int) -> int:
    """Find an element from a rotated and sorted array in ascending order.

    Args:
        a  : The sorted list to search into.
        key: The element to be found from the given list.

    Returns:
        The index of the element if found else -1.
    """
    def rotated_sorted_rec(a, k, low, high):
        if not a or low > high: return -1

        mid = (low + high) // 2
        if a[mid] == k: return mid

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
        else:
            if a[mid] != a[high]:  # left side is normally sorted
                if mid - low > 1:
                    print(f"""low:{low}; mid:{mid}, a[low]:{a[low]}; \\
                            a[mid]:{a[mid]}; a[high]:{a[high]}\n\t{a}""")
                return rotated_sorted_rec(a, k, mid + 1, high)
            else:  # unknown which side is normally sorted
                left = rotated_sorted_rec(a, k, low + 1, mid - 1)
                if left != -1: return left
                else: return rotated_sorted_rec(a, k, mid + 1, high - 1)

        # return -1

    return rotated_sorted_rec(L, key, 0, len(L) - 1)


def find_rotated_sorted_itr():
    pass


""" Find string from list of strings with interspreded empyt strings. [CtCI: 11.5].

    Write a function 'find_string_from_strings(L, s)' which takes as input a
    sorted list of strings which is interspreaded with empyt strings and a
    string 's' and returns the index of 's' in the given list.

    Examples:
        1. find_string_from_strings([], "Texas")  -> -1
        2. find_string_from_strings(["","","",""], "b")  -> -1
        3. find_string_from_strings(["a","","","","tea","up",""], "up")  -> 5
        4. find_string_from_strings(["a","","a","","","","b","b","b"], "b")  -> 6
"""


def find_string_from_strings(L: List[str], s: str) -> int:
    if not s or len(L) == 0: return -1
    low, high = 0, len(L) - 1

    while low <= high:
        mid = (low + high) // 2
        if not L[mid]:
            left, right = mid - 1, mid + 1

            while True:
                if left < low and right > high: return -1
                elif left >= low and L[left]:
                    mid = left
                    break
                elif right <= high and L[right]:
                    mid = right
                    break
                left -= 1
                right += 1

        if s < L[mid]: high = mid - 1
        elif s > L[mid]: low = mid + 1
        else: return mid


""" Find the min and max simultaneously. - [EPI: 11.7]. """


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
        global_min_max = MinMax(min(global_min_max.smallest, A[-1]),
                                max(global_min_max.largest, A[-1]))
    return global_min_max


def _test_find_min_max():
    A = []
    MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))
    find_min_max(A, MinMax)


""" Find the kth largest element. - [EPI: 11.8].

    Examples:
        1. find_kth_largest(1, [3, 1, -1, 2])   ->  3
        2. find_kth_largest(2, [3, 1, -1, 2])   ->  2
        3. find_kth_largest(3, [3, 1, -1, 2])   ->  1
        4. find_kth_largest(4, [3, 1, -1, 2])   -> -1
"""


def find_kth_largest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # NOTE: "greater than" and "less than" are defined by the comp object.
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

            if new_pivot_idx < k - 1: left = new_pivot_idx + 1
            elif new_pivot_idx > k - 1: right = new_pivot_idx - 1
            else: return A[new_pivot_idx]

        raise IndexError('no k-th node in array A')

    return find_kth(operator.gt)


""" Find the kth smallest element. - [EPI: 11.8]

    Examples:
        1. find_kth_smallest(1, [3, 1, -1, 2])  -> -1
        2. find_kth_smallest(2, [3, 1, -1, 2])  ->  1
        3. find_kth_smallest(3, [3, 1, -1, 2])  ->  2
        4. find_kth_smallest(4, [3, 1, -1, 2])  ->  3
"""


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
                    A[new_pivot_idx], A[i] = A[i], A[new_pivot_idx]
                    new_pivot_idx += 1

            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1: return A[new_pivot_idx]
            elif new_pivot_idx > k - 1: right = new_pivot_idx - 1
            else: left = new_pivot_idx + 1  # new_pivot_idx < k - 1.

        raise IndexError('no k-th node in array A')

    return find_kth(operator.lt)


""" Find the missing IP address. - [EPI: 11.9]. """


def find_missing_element(stream):

    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = itertools.tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    # Look for a bucket that contains less than (1 << 16) elements.
    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter)
                            if c < BUCKET_CAPACITY)

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


""" Find the duplicate and missing elements. - [EPI: 11.10]. """


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
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup
                                ^ miss_XOR_dup) if miss_or_dup in A else
            DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup))


def _test_find_duplicate_missing():
    A = []
    DupAndMissing = namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))
    find_duplicate_missing(A, DupAndMissing)


if __name__ == "__main__":
    pass
