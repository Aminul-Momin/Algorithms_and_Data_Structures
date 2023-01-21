from typing import Iterable
#==============================================================================
"""
Write a function 'can_sum(target_sum, numbers)' that takes a integer and an
array of numbers as arguments. The function should return boolean indicating
whether or not it is possible to generate the target_sum using the numbers

You may use an element of the array as many times as needed.
You also may assume that all the numbers in the array are nonnegative.

Examples:
    1. can_sum(7, [2, 3]) -> True
    2. can_sum(7, [5, 3, 4, 7]) -> True
    3. can_sum(7, [2, 4]) -> False
    4. can_sum(8, [2, 3, 5]) -> True
    5. can_sum(30, [7, 14]) -> False
"""
#==============================================================================


def can_sum_rec(target_sum: int, numbers: Iterable[int]) -> bool:
    """Find if it's possible to generate 'target_sum' using elements of numbers.

    Args:
        target_sum: The integer to be sumed up to.
        numbers   : A collection of numbers.

    Returns:
        True if it is possible to generate the 'target_sum' using
        elements from 'numbers' False otherwise.
    """

    if target_sum == 0: return True
    if target_sum < 0: return False

    for val in numbers:
        if can_sum_rec(target_sum - val, numbers): return True

    return False


def can_sum_memo(target_sum: int, numbers: Iterable[int], memo={}) -> bool:
    """Find if it's possible to generate `target_sum` using elements of numbers.

    Args:
        target_sum: The integer to be sumed up to.
        numbers   : A collection of numbers.

    Returns:
        True if it is possible to generate the 'target_sum' using
        elements from 'numbers' False otherwise.
    """

    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return True
    if target_sum < 0: return False
    for val in numbers:
        remaining = can_sum_memo(target_sum - val, numbers, memo)
        if remaining:
            memo[target_sum] = True
            return memo[target_sum]

    return False


def can_sum_tbl(target_sum: int, numbers: Iterable[int]) -> bool:
    """Find if it's possible to generate 'target_sum' using elements of numbers.

    Args:
        target_sum: The integer to be sumed up to.
        numbers   : A collection of numbers.

    Returns:
        True if it is possible to generate the 'target_sum' using
        elements from 'numbers' False otherwise.
    """

    tbl = [True] + [False] * target_sum

    if not target_sum: return True
    if target_sum < 0: return False

    for i in range(target_sum + 1):
        if tbl[i]:
            for val in numbers:
                if (i + val <= target_sum): tbl[i + val] = True

    return tbl[target_sum]


def main():
    test_cases = [[7, [2, 3], True], [7, [5, 3, 4, 7], True],
                  [8, [2, 3, 5], True], [7, [2, 4], False],
                  [30, [7, 14], False]]

    for target, nums, expected in test_cases:
        returned = can_sum_memo(target, nums, {})
        try:
            assert returned == expected
        except AssertionError:
            print(target, nums, expected)
            print(f'Expected: {expected}')
            print(f'Returned: {returned}')
            print()


if __name__ == '__main__':
    main()
