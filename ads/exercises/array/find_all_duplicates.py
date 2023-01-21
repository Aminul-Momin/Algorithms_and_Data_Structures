from ads.utils import swap
#==============================================================================
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

- Example 1:
    - Input: nums = [1,3,4,2,2]
    - Output: 2
- Example 2:
    - Input: nums = [3,1,3,4,2]
    - Output: 3
 

- Constraints:
    - 1 <= n <= 105
    - nums.length == n + 1
    - 1 <= nums[i] <= n
    - All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
#==============================================================================


def find_the_duplicate(a):
    N = len(a)
    i = 0

    while i < N:
        if a[i] == i + 1: i += 1
        else:
            if a[i] == a[a[i] - 1]: return a[i]
            else: swap(a, i, a[i] - 1)
    return -1


#==============================================================================
""" Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

- Example 1:
    - Input: nums = [4,3,2,7,8,2,3,1]
    - Output: [2,3]
- Example 2:
    - Input: nums = [1,1,2]
    - Output: [1]
- Example 3:
    - Input: nums = [1]
    - Output: []
 
- Constraints:
    - n == nums.length
    - 1 <= n <= 105
    - 1 <= nums[i] <= n
    - Each element in nums appears once or twice.
"""
#==============================================================================
from typing import List


def find_all_duplicates(a):
    N = len(a)
    i = 0
    while i < N:
        if a[i] == a[a[i] - 1]: i += 1
        else: swap(a, i, a[i] - 1)

    return [x for i, x in enumerate(a) if x != i + 1]


def find_duplicates(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        while nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    return [x for i, x in enumerate(nums) if x != i + 1]
