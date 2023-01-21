import math


""" Compute the integer square root. - [EPI: 11.4]. 

Examples:
    integer_square_root(0) -> 0
    integer_square_root(1) -> 1
    integer_square_root(4) -> 2
    integer_square_root(9) -> 3
    integer_square_root(16) -> 4
    integer_square_root(25) -> 5
    integer_square_root(36) -> 6
    integer_square_root(49) -> 7
    integer_square_root(64) -> 8
    integer_square_root(81) -> 9
    integer_square_root(100) -> 10
"""


def integer_square_root(k):

    left, right = 0, k
    # Candidate interval [left, right] where everything before left has square
    # <= k, everything after right has square > k.
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


""" Compute the real square root. - [EPI: 11.5].

Examples:
    real_square_root(0) -> 0.0
    real_square_root(1) -> 1.0
    real_square_root(4) -> 2.0
    real_square_root(8) -> 2.8284
    real_square_root(9) -> 3.0
    real_square_root(10) -> 3.1623
    real_square_root(15) -> 3.873
    real_square_root(16) -> 4.0
"""


def real_square_root(x):

    # Decides the search range according to x's value relative to 1.0.
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    # Keeps searching as long as left != right.
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left