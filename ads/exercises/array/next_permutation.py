""" Compute the next permutation under dictionary ordering. - [EPI: 5.11].

    There exist exactly n! permutations of n elements. These can be totally
    ordered using the 'dictionary ordering' - define permutation 'p' to appear
    before permutation 'q' if in the first place where 'p' and 'q' differ in
    their array representations, starting from index 0, the corresponding
    entry for 'p' is less than that for q. For example, [2,0,1] < [2,1,0].

    Note that the permutation [0,1,2] is the smallest and [2,1,0] is the
    largest permutation under dictionary ordering.

    Write a function 'next_permutation(P)' that takes as input a permutation,
    and return the next permutation under dictionary ordering.

    Examples:
        1. next_permutation([]) -> []
        2. next_permutation([0]) -> [0]
        3. next_permutation([0, 1]) -> [1, 0]
        4. next_permutation([2, 1, 0]) -> [2, 1, 0]
        5. next_permutation([0, 3, 1, 2]) -> [0, 3, 2, 1]
        6. next_permutation([1, 2, 4, 3, 0]) -> [1, 3, 0, 2, 4]
"""

from typing import Sequence


def next_permutation_v1(P: Sequence[int]) -> None:
    """Computes the next permutation under dictionary ordering.

    Args:
        P: The sequence of which next permutation to be computed.
    """

    if not P: return []

    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inv_point = len(P) - 2
    while inv_point >= 0 and P[inv_point] >= P[inv_point + 1]:
        inv_point -= 1

    if inv_point == -1: return []  # P is the last permutation.

    # Swap the smallest entry after index inversion_point that is greater than
    # P[inversion_point]. Since entries in P are decreasing after
    # inversion_point, if we search in reverse order, the first entry that is
    # greater than P[inversion_point] is the entry to swap with.

    for i in reversed(range(inv_point + 1, len(P))):
        if P[i] > P[inv_point]:
            P[inv_point], P[i] = P[i], P[inv_point]
            break

    # Entries in P must appear in decreasing order after inversion point,
    # so we simply reverse these entries to get the smallest dictionary order.
    P[inv_point + 1:] = reversed(P[inv_point + 1:])
