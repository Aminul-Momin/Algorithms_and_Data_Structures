from random import choice, randint

from ads.utils import load_data_from_file
#==============================================================================
""" Edit Distance

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:
    * Insert a character
    * Delete a character
    * Replace a character
 

Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
 

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""


def edit_distance_tbl(s1, s2):
    tbl = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    R, C = len(tbl), len(tbl[0])

    for i in range(R):
        for j in range(C):
            if i == 0: tbl[i][j] = j
            elif j == 0: tbl[i][j] = i
            elif s1[i - 1] == s2[j - 1]: tbl[i][j] = tbl[i - 1][j - 1]
            else:
                tbl[i][j] = 1 + min(tbl[i - 1][j - 1], tbl[i][j - 1],
                                    tbl[i - 1][j])
    return tbl[-1][-1]


# NOT COMPLETED !!
def edit_distance_memo(s1, s2):
    def key(i, j):
        return f'{i}{j}'

    def _edit_distance_memo(s1, s2, i, j, memo={}):
        if i == 0: memo[key(i, j)] = j
        elif j == 0: memo[key(i, j)] = i
        elif key(i, j) in memo: return memo[key(i, j)]
        elif i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            memo[key(i, j)] = _edit_distance_memo(s1, s2, i - 1, j - 1, memo)
        else:
            insertion = _edit_distance_memo(s1, s2, i - 1, j, memo)
            replace = _edit_distance_memo(s1, s2, i - 1, j - 1, memo)
            deletion = _edit_distance_memo(s1, s2, i, j - 1, memo)
            memo[key(i, j)] = 1 + min(insertion, replace, deletion)

        return memo[key(i, j)]

    memo = {}
    R, C = len(s1) + 1, len(s2) + 1
    _edit_distance_memo(s1, s2, R, C, memo)
    return memo[f'{R}{C}']


def main():
    word1 = choice(load_data_from_file("shellsST.txt", []))
    word2 = choice(load_data_from_file("shellsST.txt", []))

    resulted1 = edit_distance_tbl(word1, word2)
    # resulted2 = edit_distance_memo(word1, word2)
    # assert resulted1 == resulted2

    print(word1, word2, resulted1)


if __name__ == '__main__':
    main()
