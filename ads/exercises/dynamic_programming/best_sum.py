'''
Write a function `best_sum(target, nums)` that takes a `targer` and an
array of numbers as arguments. The function should return an array containing
shortest combination of elements of the given array that adds up to the `target`.

If there is no combination that adds up to the `target`, then return None.
If there is a tie for the shortest combination, then return any one combination
of the shortest combinations.

- Examples:
    1. best_sum((7, [5, 3, 4, 7])) -> [7]
    2. best_sum((8, [1, 4, 5])) -> [4, 4]
    3. best_sum((8, [2, 3, 5])) -> [5, 3]
    4. best_sum((100, [7, 14])) -> None
'''

from typing import List


def best_sum_rec(target: int, nums: List[int]) -> List[int]:
    """
    Find the shortest combination to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        numb  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """
    if target == 0: return []
    if target < 0: return None
    best_comb = None

    for num in nums:
        remaining_comb = best_sum_rec(target - num, nums)
        if remaining_comb is not None:
            cur_comb = [*remaining_comb, num]
            if not best_comb or len(cur_comb) < len(best_comb):
                best_comb = cur_comb

    return best_comb


def best_sum_memo(target: int, nums: List[int], memo={}) -> List[int]:
    """
    Find the shortest combination to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        numb  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None
    best_comb = None

    for num in nums:
        remaining_comb = best_sum_memo(target - num, nums, memo)
        if remaining_comb is not None:
            cur_comb = [*remaining_comb, num]
            if not best_comb or len(cur_comb) < len(best_comb):
                best_comb = cur_comb
    memo[target] = best_comb
    return memo[target]


def best_sum_tbl(target: int, nums: List[int]) -> List[int]:
    """
    Find the shortest combination to generate `target` using elements of nums.

    Args:
        target: The integer to be sumed up to.
        numb  : A collection of integer.

    Returns:
        Collection of integers from `nums` sum of which equal to the `target`.
    """

    tbl = [[]] + [None] * target
    N = len(tbl)

    for i in range(N):
        if tbl[i] is not None:
            for num in nums:
                if (i + num) < N:
                    this_comb = tbl[i] + [num]
                    tbl[i + num] = tbl[i + num] if (
                        tbl[i + num]
                        and len(tbl[i + num]) < len(this_comb)) else this_comb

    return tbl[target]


def main():
    pass

if __name__ == '__main__':
    main()