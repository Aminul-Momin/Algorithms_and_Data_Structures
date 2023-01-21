import itertools
from typing import List
#==============================================================================
""" Delete duplicates from a sorted Array. - [EPI: 5.5].

Examples:
    1. delete_duplicate([]) -> []
    2. delete_duplicate([1]) -> [1]
    3. delete_duplicate([2, 4]) -> [2, 4]
    4. delete_duplicate([1, 4, 5]) -> [1, 4, 5]
    5. delete_duplicate([1, 1, 3, 5]) -> [1, 3, 5]
    6. delete_duplicate([1, 1, 2, 4, 5]) -> [1, 2, 4, 5]
    7. delete_duplicate([1, 1, 2, 3, 5, 5]) -> [1, 2, 3, 5]
    8. delete_duplicate([1, 1, 1, 1, 3, 3, 5]) -> [1, 3, 5]
    9. delete_duplicate([1, 2, 3, 3, 4, 4, 4, 5]) -> [1, 2, 3, 4, 5]
    10. delete_duplicate([1, 1, 2, 3, 3, 3, 4, 5, 5]) -> [1, 2, 3, 4, 5]
"""


def delete_duplicates(A: List) -> None:
    """Remove the duplicate elements from the given list.

    Args:
        A: Sorted list of integer.
    """

    A.sort()  # Makes identical elements become neighbors.
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx - 1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]


def delete_duplicates_pythonic(A: List) -> None:
    """Remove the duplicate elements from the given list.

    Args:
        A: Sorted list of integer.
    """

    A.sort()
    write_idx = 0
    for cand, _ in itertools.groupby(A):
        A[write_idx] = cand
        write_idx += 1
    del A[write_idx:]
