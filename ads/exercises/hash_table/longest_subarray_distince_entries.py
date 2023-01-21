""" Find the longest subarray with distinct entries. - [EPI:12.9].

Write a program that takes an array and returns the length of a longest
subarray with the property that all its elements are distinct.

For example,if the array is (f,s,f,e,t,w,e,n,w,e) then a longest subarray all
of whose elements are distinct is (s,f,e,t,w).

Hint: What should you do if the subarray from indices i to j satisfies the
property, but the subarray from i to j+1 does not?
"""


def longest_subarray_with_distinct_entries(A):

    # Records the most recent occurrences of each entry.
    most_recent_occurrence = {}
    longest_dup_free_subarray_start_idx = result = 0
    for i, a in enumerate(A):
        # Defer updating dup_idx until we see a duplicate.
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            # A[i] appeared before. Did it appear in the longest current
            # subarray?
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1
        most_recent_occurrence[a] = i
    return max(result, len(A) - longest_dup_free_subarray_start_idx)


def main():
    pass


if __name__ == '__main__':
    main()