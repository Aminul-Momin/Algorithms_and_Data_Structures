from random import randint, sample
from collections import Counter
from typing import List
from ads.utils import print_matrix
#==============================================================================
"""Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

It is guaranteed that the number of unique combinations that sum up to target is
less than 150 combinations for the given input.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.
Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:
    Input: candidates = [2], target = 1
    Output: []
Example 4:
    Input: candidates = [1], target = 1
    Output: [[1]]
Example 5:
    Input: candidates = [1], target = 2
    Output: [[1,1]]
 

Constraints:

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    All elements of candidates are distinct.
    1 <= target <= 500

"""


def com_sum(nums, target):
    pass


""" Combination Sum II

Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output:
    [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output:
    [[1,2,2],[5]]
 

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""


def comb_sum(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(comb, remain, curr, counter, results):
        if remain == 0:
            # make a deep copy of the current combination
            #   rather than keeping the reference.
            results.append(list(comb))
            return None
        elif remain < 0:
            return None

        for next_curr in range(curr, len(counter)):
            candidate, freq = counter[next_curr]

            if freq <= 0:
                continue

            # add a new element to the current combination
            comb.append(candidate)
            counter[next_curr] = (candidate, freq - 1)

            # continue the exploration with the updated combination
            backtrack(comb, remain - candidate, next_curr, counter, results)

            # backtrack the changes, so that we can try another candidate
            counter[next_curr] = (candidate, freq)
            comb.pop()

    results = []  # container to hold the final combinations
    counter = Counter(nums)
    # convert the counter table to a list of (num, count) tuples
    counter = [(c, counter[c]) for c in counter]

    backtrack(comb=[], remain=target, curr=0, counter=counter, results=results)

    return results


def comb_sum_v2(nums: List[int], target: int) -> List[List[int]]:
    def backtrack(comb, remain, curr, results):

        if remain == 0:
            # make a deep copy of the resulted combination
            results.append(list(comb))
            return

        for next_curr in range(curr, len(nums)):

            if next_curr > curr \
              and nums[next_curr] == nums[next_curr-1]:
                continue

            pick = nums[next_curr]
            # optimization: skip the rest of elements starting from 'curr' index
            if remain - pick < 0:
                break

            comb.append(pick)
            backtrack(comb, remain - pick, next_curr + 1, results)
            comb.pop()

    nums.sort()

    comb, results = [], []
    backtrack(comb, target, 0, results)

    return results


""" Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain
the same combination twice, and the combinations may be returned in any order.

 

Example 1:
    Input: k = 3, n = 7
    Output: [[1,2,4]]
    Explanation:
    1 + 2 + 4 = 7
    There are no other valid combinations.
Example 2:
    Input: k = 3, n = 9
    Output: [[1,2,6],[1,3,5],[2,3,4]]
    Explanation:
    1 + 2 + 6 = 9
    1 + 3 + 5 = 9
    2 + 3 + 4 = 9
    There are no other valid combinations.
Example 3:
    Input: k = 4, n = 1
    Output: []
    Explanation: There are no valid combinations.
    Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
Example 4:
    Input: k = 3, n = 2
    Output: []
    Explanation: There are no valid combinations.
Example 5:
    Input: k = 9, n = 45
    Output: [[1,2,3,4,5,6,7,8,9]]
    Explanation:
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
    There are no other valid combinations.
    

Constraints:
    2 <= k <= 9
    1 <= n <= 60

"""