'''
Write a function `how_sum(target, nums)` that takes a `target` and an
array of numbers as arguments. The function should return an array containing
any combination of elements of the given array that adds up to the `target`.

If there is no combination that adds up to the `target`, then return None.
If there are multiple combination, then return any one combination.

- Examples:
    1. how_sum((7, [2, 3])) -> [3, 2, 2]
    2. how_sum((7, [5, 3, 4, 7])) -> [4, 3]
    3. how_sum((7, [2, 4])) -> None
    4. how_sum((8, [2, 3, 5])) -> [2, 2, 2, 2]
    5. how_sum((100, [7, 14])) -> None
'''

from typing import List
import time
from functools import lru_cache


def how_sum_rec(target: int, nums: List[int]) -> List[int]:
    """Find the path if it's possible to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        numb  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """
    if target == 0: return []
    if target < 0: return None

    for num in nums:
        remaining = how_sum_rec(target - num, nums)
        if remaining is not None: return [num, *remaining]

    return None


# NOT WORKING !!
def how_sum_memo(target: int, nums: List[int], memo={}) -> List[int]:
    """Find the path if it's possible to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        numb  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for num in nums:
        remaining = how_sum_memo(target - num, nums, memo)
        if remaining is not None:
            memo[target] = [num, *remaining]
            return memo[target]
    memo[target] = None
    return memo[target]


def how_sum_tbl(target, nums):
    """Find the path if it's possible to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        nums  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """

    tbl = [[]] + [None] * target

    for i in range(len(tbl)):
        if tbl[i] is not None:
            for num in nums:
                if (i + num) < len(tbl):
                    tbl[i + num] = [num] + tbl[i]

    return tbl[target]


def how_sum_rec_2(target: int, nums: List[int]) -> List[int]:
    """Find the path if it's possible to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        numb  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """
    def _how_sum_rec_2(target, nums, cur_sum, chosen):
        if cur_sum > target: return None
        if cur_sum == target: return chosen
        for num in nums:
            chosen.append(num)
            cur_res = _how_sum_rec_2(target, nums, cur_sum + num, chosen)
            if cur_res: return cur_res
            else: chosen.pop()

    return _how_sum_rec_2(target, nums, 0, [])


def main():

    L = [[7, [2, 3], [2, 2, 3]], [7, [5, 3, 4, 7], [3, 4]], [7, [2, 4], None],
         [8, [2, 3, 5], [2, 2, 2, 2]], [100, [7, 14], None]]
    for target, nums, expected in L:
        # print(target, nums, expected, how_sum_memo(target, nums))
        assert how_sum_rec(target, nums) == expected
        assert how_sum_rec_2(target, nums) == expected
        assert how_sum_memo(target, nums, {}) == expected
        assert how_sum_tbl(target, nums) == expected


if __name__ == '__main__':
    main()
