from random import randint

#==============================================================================
""" Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both
strings.

 
- Example 1:
    - Input: text1 = "abcde", text2 = "ace"
    - Output: 3
    - Explanation: The longest common subsequence is "ace" and its length is 3.

- Example 2:
    - Input: text1 = "abc", text2 = "abc"
    - Output: 3
    - Explanation: The longest common subsequence is "abc" and its length is 3.

- Example 3:
    - Input: text1 = "abc", text2 = "def"
    - Output: 0
    - Explanation: There is no such common subsequence, so the result is 0.


- Constraints:
    - 1 <= text1.length, text2.length <= 1000
    - text1 and text2 consist of only lowercase English characters.
"""


def lcs_rec(seq1: str, seq2: str):
    def _lcs_rec(i: int, j: int):
        if i >= len(seq1) or j >= len(seq2): return 0
        elif seq1[i] == seq2[j]: return 1 + _lcs_rec(i + 1, j + 1)
        else: return max(_lcs_rec(i + 1, j), _lcs_rec(i, j + 1))

    return _lcs_rec(0, 0)


def lcs_tbl(text1: str, text2: str):
    M = len(text1)
    N = len(text2)
    tbl = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if text1[i - 1] == text2[j - 1]:
                tbl[i][j] = 1 + tbl[i - 1][j - 1]
            else:
                tbl[i][j] = max(tbl[i - 1][j], tbl[i][j - 1])
    return tbl[-1][-1]


def main():
    L = [["abdace", "babce"], ["stone", "longest"]]
    for seq1, seq2 in L:
        res_req = lcs_rec(seq1, seq2)
        res_tbl = lcs_tbl(seq1, seq2)
        print(res_req, res_tbl)


if __name__ == '__main__':
    main()
