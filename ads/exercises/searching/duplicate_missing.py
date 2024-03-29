from collections import namedtuple
from functools import reduce
#==============================================================================
"""
You are given an array of z integers, each between 0 and n - 1., inclusive. Exactly one elementaPpears twice, implying that exactly one number between 0 and n - 1 is missing from the array.How would you compute the duplicate and missing numbers?
Hint: Consider performing multiple passes through the array.
"""


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


def main():
    A = []
    DupAndMissing = namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))
    find_duplicate_missing(A, DupAndMissing)


if __name__ == '__main__':
    main()
