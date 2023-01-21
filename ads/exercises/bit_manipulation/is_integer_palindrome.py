import math
from random import randint
#==============================================================================
""" Check if a decimal integer is a palindrome. [EPI:9]

    Write a function 'is_integer_palindrome(x)' which takes an integer and
    determines if that integer's representation as a decimal string is a
    palindrom.

    Examples:
        1. is_palindrome_number(0)          -> True
        2. is_palindrome_number(11)         -> True
        3. is_palindrome_number(121)        -> True
        4. is_palindrome_number(333)        -> True
        5. is_palindrome_number(2147447412) -> True
        6. is_palindrome_number(-1)         -> False
        7. is_palindrome_number(12)         -> False

"""


def is_integer_palindrome(x):

    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask  # Remove the most significant digit of x.
        x //= 10  # Remove the least significant digit of x.
        msd_mask //= 100
    return True


def main():
    testing_over = [[0, True], [-0, True], [-1, False], [00, True],
                    [10101, True], [101, True], [-1111, False], [1111, True]]

    for given, expected in testing_over:
        returned = is_integer_palindrome(given)
        print(returned, expected)
        assert returned == expected


if __name__ == '__main__':
    main()
