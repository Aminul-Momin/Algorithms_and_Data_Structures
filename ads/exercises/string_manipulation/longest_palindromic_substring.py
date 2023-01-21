from random import choice, randint

#==============================================================================
""" Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


- Example 1:
    - Input: s = "babad"
    - Output: "bab"
    - Note: "aba" is also a valid answer.

- Example 2:
    - Input: s = "cbbd"
    - Output: "bb"

- Example 3:
    - Input: s = "a"
    - Output: "a"

- Example 4:
    - Input: s = "ac"
    - Output: "a"

- Constraints:
    1) 1 <= s.length <= 1000
    2) s consist of only digits and English letters (lower-case and/or upper-case),
"""
#==============================================================================


def expend_around_center(s: str, low, high) -> int:
    if not s or low > high: return 0

    while low >= 0 and high < len(s) and s[low] == s[high]:
        low -= 1
        high += 1

    return high - low - 1


def lps_sliding_window(s: str) -> str:
    """Find longest plindromic substring.

    Args:
        s (str): [description]
    """
    if not s or len(s) < 1: return ""
    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expend_around_center(s, i, i)
        len2 = expend_around_center(s, i, i + 1)
        length = max(len1, len2)
        print(i, length)
        if length > (end - start):
            start = i - (length - 1) // 2
            end = i + length // 2

    return s[start:end + 1]


def len_lps_dp(s: str):
    N = len(s)
    tbl = [[False] * N for _ in range(N)]
    length = 0

    for g in range(N):
        for i, j in zip(range(N), range(g, N)):
            if g == 0: tbl[i][j] = True
            elif g == 1:
                if s[i] == s[j]: tbl[i][j] = True
                else: tbl[i][j] = False
            else:
                if s[i] == s[j] and tbl[i + 1][j - 1]: tbl[i][j] = True
                else: tbl[i][j] = False

            if tbl[i][j]: length = g + 1
    return length


# A Python3 solution for longest palindrome


# Function to pra subString str[low..high]
def printSubStr(str, low, high):

    for i in range(low, high + 1):
        print(str[i], end="")


# This prints the longest palindromic subString and returns it's length.
def lps_v2(str):

    # Get length of input String
    n = len(str)

    # All subStrings of length 1
    # are palindromes
    maxLength = 1
    start = 0

    # Nested loop to mark start
    # and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1

            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0

            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1

    # print("Longest palindrome subString is: ", end="")
    # printSubStr(str, start, start + maxLength - 1)

    # Return length of LPS
    # return maxLength
    return str[start:start + maxLength + 1]


def main():
    from string import ascii_uppercase as UPPERCASE

    # s = ''.join([choice(UPPERCASE) for i in range(20)])
    s = 'racecaree'
    # print(lps(s))
    print(lps_v2(s))
    # print(len_lps_dp(s))


if __name__ == '__main__':
    main()
