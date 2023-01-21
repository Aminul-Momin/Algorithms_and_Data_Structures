from random import choice
#==============================================================================
""" Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R'
characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

- Example 1:
    - Input: s = "RLRRLLRLRL"
    - Output: 4
    - Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

- Example 2:
    - Input: s = "RLLLLRRRLR"
    - Output: 3
    - Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

- Example 3:
    - Input: s = "LLLLRRRR"
    - Output: 1
    - Explanation: s can be split into "LLLLRRRR".

- Example 4:
    - Input: s = "RLRRRLLRLL"
    - Output: 2
    - Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 

- Constraints:
    1) 1 <= s.length <= 1000
    2) s[i] is either 'L' or 'R'.
    3) s is a balanced string.

"""


def balanced_str_split(s: str) -> int:

    num_balanced_str = 0
    count = 0

    for c in s:
        if c == 'L': count += 1
        if c == 'R': count -= 1
        if count == 0: num_balanced_str += 1
    return num_balanced_str


def main():
    s = ''.join([choice(('L', 'R')) for i in range(10)])
    returned = balanced_str_split(s)

    print(s, returned, sep='\t')


if __name__ == '__main__':
    main()
