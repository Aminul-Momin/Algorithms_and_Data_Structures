from typing import List
#==============================================================================
"""
Given an array of positive numbers `nums` and a positive number `target`, find
the length of the smallest contegious subarray whose sum is greater than or
equal `target`. Return 0 if no such subarray exists.
"""
#==============================================================================


def len_contegious_subarray(nums: List[int], target: int):
    res = {'min_win_len': 0}
    left, win_sum = 0, 0

    for right, val in enumerate(nums):
        win_sum += val
        while win_sum >= target:
            cur_win_len = right - left + 1
            res['min_win_len'] = cur_win_len
            res['left_idx'] = left
            res['right_idx'] = right

            win_sum -= nums[left]
            left += 1
    return res['min_win_len']


def main():
    L = [[[1, 3, 2, 2, 4, 5], 6, 2], [[2, 1, 5, 2, 8], 7, 1]]
    for nums, target, expected in L:
        assert len_contegious_subarray(nums, target) == expected


if __name__ == '__main__':
    main()
