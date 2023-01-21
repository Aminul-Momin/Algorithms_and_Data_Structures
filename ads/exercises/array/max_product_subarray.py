from random import randint
from typing import List

#==============================================================================
"""
152. Maximum Product Subarray

Given an integer array nums, find a CONTIGUOUS non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a CONTIGUOUS subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


def max_prod_subarray(nums: List[int]) -> int:
    max_prod = max(nums)
    cur_max, cur_min = 1, 1

    for num in nums:
        tmp = num * cur_max
        cur_max = max(tmp, cur_min * num, num)
        cur_min = min(tmp, cur_min * num, num)
        max_prod = max(max_prod, cur_max)

    return max_prod


def max_prod_subarray_v2(nums: List[int]) -> int:
    max_prod = nums[0]
    cur_max, cur_min = nums[0], nums[0]

    for num in nums[1:]:
        tmp = num * cur_max
        cur_max = max(tmp, cur_min * num, num)
        cur_min = min(tmp, cur_min * num, num)
        max_prod = max(max_prod, cur_max)

    return max_prod


def main():
    nums = [randint(-10, 10) for _ in range(10)]
    returned = max_prod_subarray(nums)
    print(nums, returned)


if __name__ == '__main__':
    main()
