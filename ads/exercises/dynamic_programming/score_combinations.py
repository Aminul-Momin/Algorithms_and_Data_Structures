from random import randint, sample
from collections import Counter
from typing import List
# from ads.utils import print_matrix

#==============================================================================
#==============================================================================
"""
In an American Football game, a play can lead to the following score
- 2 points (safety)
- 3 points (field goal)
- 7 points (touchdown, assuming the extra point).

Many different combination of [2,3,7] points can make up a final score.

- Example:
    - four combinations of plays yield a score of 12:
        - 6 safety (2x6);
        - 4 field goal (4x3);
        - 1 safwty, 1 field goal and  1 touchdown (2+3+7); and
        - 3 safety and 2 field goal (3x2 + 2x3).

Write a program that takes a final score and scores for individual plays, and
returns the number of combinations of plays that result in the final score.
- [EPI: 16.1].
"""

def num_score_comb_memo(final_scores, L):
    def _score_comb_memo_v_1(i, j, L, memo={}):
        key = F"{i},{j}"
        if key in memo: return memo[key]
        if i == j == 0: return 1
        if i < 0 or j < 0: return 0

        _without = _score_comb_memo_v_1(i - 1, j, L, memo)
        _with = _score_comb_memo_v_1(i, j - L[i], L, memo)  # if j >= L[i] else 0
        memo[key] = _without + _with

        return memo[key]

    def _score_comb_memo_v_2(i, j, L, matrix):
        if matrix[i][j]: return matrix[i][j]
        if i < 0: return 0
        _without = _score_comb_memo_v_2(i - 1, j, L, matrix)
        _with = _score_comb_memo_v_2(i, j - L[i], L, matrix) if j >= L[i] else 0
        matrix[i][j] = _without + _with

        return matrix[i][j]

    M = [[1] + [0] * final_scores for _ in L]
    return _score_comb_memo_v_2(len(L) - 1, final_scores, L, M)
    # return _score_comb_memo_v_1(len(L)-1, final_scores, L)


def num_score_comb_tbl_v_1(target, nums):

    # One way to reach 0. M -> num_score_combinations
    M = [[1] + [0] * target for _ in nums]

    for i in range(len(nums)):
        for j in range(1, target + 1):
            _without_this_shot = M[i - 1][j] if i >= 1 else 0
            with_this_shot = M[i][j - nums[i]] if j >= nums[i] else 0

            M[i][j] = _without_this_shot + with_this_shot

    return M[-1][-1]


def num_score_comb_tbl_v_2(target: int, nums: List[int]) -> int:
    tbl = [1] + [0 for _ in range(target)]

    for val in nums:
        for i in range(val, target + 1):
            tbl[i] += tbl[i - val]
        print(tbl)
    return tbl[-1]



def num_score_comb_tbl_v_3(target, nums):
    tbl = [1] + [0 for _ in range(target)]

    for val in nums:
        for i in range(target + 1):
            if i - val >= 0: tbl[i] += tbl[i - val]
    return tbl[-1]



def num_score_comb_tbl_v_4(target: int, nums: List[int]) -> int:

    tbl = [1] + [0] * target

    if not target: return 1
    if target < 0: return -1

    for val in nums:
        for i in range(target + 1):
            if tbl[i] and (i + val <= target): tbl[i + val] += tbl[i]

    return tbl[-1]

    # in process of construction
def num_score_comb_tbl_v_5(target, L):

    M = [[1] + [0] * target for i in range(len(L) + 1)]

    for i in range(1, len(L)):
        for j in range(1, target + 1):
            without_this_shot = M[i - 1][j]
            with_this_shot = M[i][j - L[i]] if j >= L[i] else 0
            M[i][j] = without_this_shot + with_this_shot

    return M[-1][-1]


def _test_num_score_comb():

    target = randint(10, 30)
    L = sample(range(1, 10), 6)
    target = 6
    L = [2, 4, 6]
    returned = num_score_comb_tbl_v_2(target, L)


if __name__ == '__main__':
    _test_num_score_comb()
