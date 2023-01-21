from random import randint, sample
from typing import List
from typing_extensions import final
from ads.utils import print_matrix
#==============================================================================
#==============================================================================
""" 
Combination Sum IV (Score Combinations - [EPI: 16.1].)

Given an array of distinct integers `nums` and a target integer `target`, return
the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

- Example 1:
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation: The possible combination ways are:
        - (1, 1, 1, 1)
        - (1, 1, 2)
        - (1, 2, 1)
        - (1, 3)
        - (2, 1, 1)
        - (2, 2)
        - (3, 1)
    
    NOTE: different sequences are counted as different combinations.

- Example 2:
    Input: nums = [9], target = 3
    Output: 0
 
- Constraints:
    1. 1 <= nums.length <= 200
    1. 1 <= nums[i] <= 1000
    1. All the elements of nums are unique.
    1. 1 <= target <= 1000
 
Follow up: What if negative numbers are allowed in the given array? How does
it change the problem? What limitation we need to add to the question to allow
negative numbers?
"""


def comb_sum_memo(target: int, nums: List[int]):
    memo = {0: 1}

    for total in range(1, target + 1):
        memo[total] = 0
        for num in nums:
            memo[total] += memo.get(total - num, 0)
    return memo[target]


def comb_sum_tbl(target_sum: int, nums: List[int]) -> bool:

    tbl = [1] + [0] * target_sum

    if not target_sum: return True
    if target_sum < 0: return False

    for i in range(target_sum + 1):
        if tbl[i]:
            for val in nums:
                if (i + val <= target_sum): tbl[i + val] += tbl[i]

    return tbl[target_sum]


def comb_sum_tbl_v2(target, nums):

    if not target: return 0
    if target < 0: return 0

    tbl = [1] + [0 for _ in range(target)]

    for i in range(target + 1):
        for val in nums:
            # tbl[i] += tbl[i - val]  # WHY NO ERROR !!!!
            if i - val >= 0: tbl[i] += tbl[i - val]
    return tbl[-1]


def main():
    # target = randint(10, 30)
    # L = sample(range(1, 10), 6)

    target = 12
    L = [2, 3, 7]
    res1 = comb_sum_memo(target, L)
    res2 = comb_sum_tbl(target, L)
    res3 = comb_sum_tbl_v2(target, L)
    assert res1 == res2 == res3

    print(target, L)
    print(res1, res2, res3)


if __name__ == '__main__':
    main()
