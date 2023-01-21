#==============================================================================
"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements. For
example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

- Example 1:
    - Input: nums = [10,9,2,5,3,7,101,18]
    - Output: 4
    - Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
- Example 2:
    - Input: nums = [0,1,0,3,2,3]
    - Output: 4
- Example 3:
    - Input: nums = [7,7,7,7,7,7,7]
    - Output: 1
- Constraints:
    - 1 <= nums.length <= 2500
    - -104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
#==============================================================================

from random import randint


def lis(nums):
    N = len(nums)
    tbl = [1] * N

    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            if nums[i] < nums[j]:
                tbl[i] = max(tbl[i], 1 + tbl[j])
    return max(tbl)


def lis_v2(L):
    N = len(L)
    tbl = [1] * N

    for i in range(N):
        subproblems = [tbl[j] for j in range(i) if L[j] < L[i]]
        tbl[i] = 1 + max(subproblems, default=0)
    return max(tbl, default=0)


# Under Construction !!
def lon_incr_subseq_memo(nums, n, memo={}):
    if not nums: return 0
    if n in memo: memo[n]
    if n == 0: return 1

    cur_max = 0

    for j in range(n):
        if nums[j] < nums[n]:
            cur_max = max(lon_incr_subseq_memo(nums, n - 1, memo={}), cur_max)
    memo[n] = 1 + cur_max
    return memo[n]


def main():
    L = [randint(-10, 10) for _ in range(10)]
    res1 = lis(L)
    res2 = lis(L)
    res3 = lon_incr_subseq_memo(L, len(L) - 1, memo={})
    print(res1, res3)
    assert res1 == res2


if __name__ == '__main__':
    main()
