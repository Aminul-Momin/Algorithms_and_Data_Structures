"""
Given a string, find the length of the longest substring that contains no
more than `k` distinct characters.

- Example:
    - len_longest_substring("acccpbbebi", 3) -> 6
    - len_longest_substring("aaaabbcccd", 1) -> 4
    - len_longest_substring("abcdefg", 10)   -> 7
"""

import sys


def len_longest_substring(text: str, k: int):
    char_count = {}
    left = 0
    res = [0, -1, -1]

    for right, char in enumerate(text):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = text[left]
            char_count[left_char] -= 1
            if char_count[left_char] <= 0: del char_count[left_char]
            left += 1

        cur_win_len = right - left + 1
        if cur_win_len > res[0]:
            res[0] = cur_win_len
            res[1], res[2] = left, right
    return res


def main():
    test_cases = [["acccpbbebi", 3, 6], ["aaaabbcccd", 1, 4],
                  ["abcdefg", 10, 7], ['', 3, 0]]

    for text, k, expected in test_cases:
        result = len_longest_substring(text, k)
        assert result[0] == expected
        # print(result)


if __name__ == '__main__':
    main()
