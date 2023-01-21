import string
from functools import reduce
""" Interconvert strings and integers. - [EPI: 6.1].

    Write two functions 'int_to_str_v1(x: int)' and 'str_to_int_v1(s: str)', 
    first of which takes an integer as input and returns string form of that
    integer and second of which takes string form of an integer and returns
    that integer.

    Examples:
        Integer to String Conversion:
            1. int_to_str(0) -> "0"
            2. int_to_str(-1) -> "-1"
            3. int_to_str(-8318) -> "-8318"
            4. int_to_str(-10411) -> "-10411"

        String to Integer Conversion:
            1. str_to_int("0") -> 0
            2. str_to_int("-1") -> -1
            3. str_to_int("-8318") -> -8318
            4. str_to_int("-10411") -> -10411
"""


def int_to_str_v1(n: int) -> str:
    """Convert the given integer into it's string form.

    Args:
        n: The integer whose string form to be gotten.

    Returns:
        The string form of the given integer.
    """

    is_negative = False
    if n < 0:
        n, is_negative = -n, True

    s = []
    while True:
        s.append(chr(ord('0') + n % 10))
        n //= 10
        if n == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def int_to_str_v2(n: int) -> str:
    """Convert the given integer into it's string form.

    Args:
        n: The integer whose string form to be gotten.

    Returns:
        The string form of the given integer.
    """

    if n == 0: return '0'
    sign, n = ('-', -n) if n < 0 else ('', n)

    s = []
    while n > 0:
        s.append(chr(ord('0') + n % 10))
        n = n // 10

    return sign + ''.join(reversed(s))


def str_to_int_v1(s: str) -> int:
    """Convert the given string into it's integer form.

    Args:
        s: The string whose integer form to be gotten.

    Returns:
        The integer form of the given string.
    """

    res = 0
    sign = -1 if s[0] == '-' else 1
    s = s[s[0] == '-':]
    for i in s:
        res = res * 10 + string.digits.index(i)
    return sign * res


def str_to_int_v2(s: str) -> int:
    """Convert the given string into it's integer form.

    Args:
        s: The string whose integer form to be gotten.

    Returns:
        The integer form of the given string.
    """

    res = 0
    initial_point = 0 if s[0] is not '-' else 1

    for i in range(initial_point, len(s)):
        cur_digit = ord(s[i]) - ord('0')
        res = res * 10 + cur_digit

    return (res if not initial_point else -res)


def str_to_int_v3(s: str) -> int:
    """Convert the given string into it's integer form.

    Args:
        s: The string whose integer form to be gotten.

    Returns:
        The integer form of the given string.
    """

    sign = -1 if s[0] == '-' else 1
    s = s[s[0] == '-':]
    callback = lambda res, item: res * 10 + string.digits.index(item)
    res = reduce(callback, s, 0)
    # print(res, sign)
    return res * sign


def main():
    pass


if __name__ == '__main__':
    main()