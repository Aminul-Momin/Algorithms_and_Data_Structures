#==============================================================================
""" Find the longest subarray with distinct entries. - [EPI:12.9].

Write a program that takes an array and returns the length of a longest
subarray with the property that all its elements are distinct.

- Example
    - Input: [f,s,f,e,t,w,e,n,w,e]
    - Output: 5; a longest subarray is [s,f,e,t,w].

`Hint`: What should you do if the subarray from indices i to j satisfies the
property, but the subarray from i to j+1 does not?
"""
#==============================================================================


def longest_subarray_with_distinct_entries(A):

    # Records the most recent occurrences of each entry.
    most_recent_occurrence = {}

    left = 0  # longest_dup_free_subarray_start_idx
    result = 0

    for right, cur_elm in enumerate(A):

        # Defer updating `prev_occurance_idx` until we see a duplicate.
        if cur_elm in most_recent_occurrence:
            prev_occurance_idx = most_recent_occurrence[cur_elm]

            # Did `cur_elm` appear in the longest current subarray?
            if prev_occurance_idx >= left:
                result = max(result, right - left)
                left = prev_occurance_idx + 1

        most_recent_occurrence[cur_elm] = right

    return max(result, len(A) - left)


def main():
    L = [[[43, 43], 1], [[1, 1, 1], 1], [[1, 2, 1], 2],
         [[1, 2, 1, 3, 1, 2, 1], 3], [[1, 2, 2, 3, 3, 1, 1, 2, 1], 2],
         [[26, 73, 77, 26, 73, 77, 73, 73], 3], [[8, 8, 8, 8, 8], 1],
         [[87, 27, 27, 76, 84, 27], 3], [[], 0], [[57], 1]]

    for nums, expected in L:
        assert longest_subarray_with_distinct_entries(nums) == expected


if __name__ == '__main__':
    main()
