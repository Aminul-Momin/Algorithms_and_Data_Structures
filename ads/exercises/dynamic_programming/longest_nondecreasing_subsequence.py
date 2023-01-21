from typing import List
#==============================================================================
"""
Write a function `len_lns(nums)` (length of longest nondecreasing subsequence)
which takes as input an array of numbers `nums` and return the length of a
longest nondecreassing subsequence in the array.
"""
#==============================================================================

def longest_nondecreasing_subsequence_length(nums):

    # max_length[i] holds the length of the longest nondecreasing subsequence
    # of nums[:i + 1].
    max_length = [1] * len(nums)
    for i in range(1, len(nums)):
        max_length[i] = 1 + max(
            (max_length[j] for j in range(i) if nums[i] >= nums[j]), default=0)
    return max(max_length)


def main():
    pass


if __name__ == '__main__':
    main()
