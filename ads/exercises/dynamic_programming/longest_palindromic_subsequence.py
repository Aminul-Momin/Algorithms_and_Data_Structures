""" Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

- Example 1:
    - Input: s = "bbbab"
    - Output: 4
    - Explanation: One possible longest palindromic subsequence is "bbbb".
- Example 2:
    - Input: s = "cbbd"
    - Output: 2
    - Explanation: One possible longest palindromic subsequence is "bb".
- Constraints:
    - 1 <= s.length <= 1000
    - s consists only of lowercase English letters.
"""
#==============================================================================
import time

def lps_tbl_v1(s: str) -> int:
    if not s: return 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in reversed(range(n)):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1] + 2
            else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def main():
    test_cases = [["", 0], ['aaaaab', 5], ['aacccccbbbb', 5]]
    for test_case, expected in test_cases:
        returned = lps_tbl_v1(test_case)
        # assert returned == expected
        # assert returned == lps_memo(test_case)
        # assert returned == lps_rec(test_case)
        # assert returned == lps_tbl_v2(test_case)



if __name__ == '__main__':
    main()