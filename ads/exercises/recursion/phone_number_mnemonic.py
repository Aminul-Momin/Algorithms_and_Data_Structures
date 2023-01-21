from typing import Container, Sequence
import string
#==============================================================================
"""
Implementation of the phone number mnemonics. - [EPI: 6.7].

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent. Return the answer in any
order.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

- Example 1:
    - Input: digits = "23"
    - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Example 2:
    - Input: digits = ""
    - Output: []
- Example 3:
    - Input: digits = "2"
    - Output: ["a","b","c"]
 
- Constraints:
    - 0 <= digits.length <= 4
    - digits[i] is a digit in the range ['2', '9'].
"""


def phone_mnemonic(phn_num: str) -> Container[Sequence]:
    def _phone_mnemonics(phn_num: str,
                         k: int,
                         MAPPING: tuple,
                         result,
                         prefix=""):
        if k == len(phn_num):
            result.append(prefix)
        else:
            for i in MAPPING[string.digits.index(phn_num[k])]:
                _phone_mnemonics(phn_num, k + 1, MAPPING, result, prefix + i)

    MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV',
               'WXYZ')
    result = []
    _phone_mnemonics(phn_num, 0, MAPPING, result)
    return result


def main():
    pass


if __name__ == '__main__':
    main()