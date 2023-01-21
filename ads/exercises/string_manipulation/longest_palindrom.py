from random import randint
#==============================================================================
"""
Given a string s which consists of lowercase or uppercase letters, return the 
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


- Example 1:
    - Input: s = "abccccdd"
    - Output: 7
    - Explanation: One longest palindrome that can be built is "dccaccd", whose
      length is 7.

- Example 2:
    - Input: s = "a"
    - Output: 1

- Example 3:
    - Input: s = "bb"
    - Output: 2

- Constraints:

    - 1 <= s.length <= 2000
    - s consists of lowercase and/or uppercase English letters only.
"""
#==============================================================================


def len_longest_palindrom(s: str):

    char_count = {}
    for char in s:
        char_count[char] = char_count[char] + 1 if char in char_count else 1

    is_odd = False
    length = 0
    for char, count in char_count.items():
        if count % 2 == 0: length += count
        else:
            is_odd = True
            length += count - 1
    if is_odd: length += 1
    return length


def main():
    res = len_longest_palindrom("abccccdd")
    assert res == 7


if __name__ == '__main__':
    main()
