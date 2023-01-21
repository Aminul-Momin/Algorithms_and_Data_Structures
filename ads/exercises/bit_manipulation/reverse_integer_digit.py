from random import randint
from ece.utils import load_json_data
#==============================================================================
""" Reverse digits. [EPI:8]

Write a program which takes an integer and returns the integer corresponding
to the digits of input written in reverse order.

Examples:
    reverse_integer_digit(0) -> 0
    reverse_integer_digit(-10000) -> -1
    reverse_integer_digit(-8085) -> -5808
    reverse_integer_digit(10577) -> 77501
    reverse_integer_digit(460) -> 64
    reverse_integer_digit(-85) -> -58
    reverse_integer_digit(10154) -> 45101
    reverse_integer_digit(-12591) -> -19521
"""


def reverse_integer_digit(x):

    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


def main():
    for i in range(0, 100001, 10000):
        given = randint(-i, i)

        if given < 0:
            expected_string = '-' + ''.join([*reversed(list(str(given * -1)))])
        else:
            expected_string = ''.join([*reversed(list(str(given)))])

        expected = int(expected_string)
        returned = reverse_integer_digit(given)
        assert returned == expected


if __name__ == '__main__':
    main()
