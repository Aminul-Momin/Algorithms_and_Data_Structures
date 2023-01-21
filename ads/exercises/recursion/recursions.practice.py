from random import randrange, randint
from typing import Container, Sequence, List
from functools import reduce
from itertools import accumulate, groupby
import sys

from ads.utils import swap, print_matrix  # added through the PYTHONPATH variable
import recursions as Rec
"""Implement a program that prints all the n-digits binary numbers."""


def print_binary(digits):
    pass


def _print_binary(digits, prefix):
    pass


""" Implement a program that prints all the n-digits decimal numbers."""


def print_decimal(digits):
    pass


def _print_decimal(digits, prefix):
    pass


"""You have d dice, and each die has f faces numbered 1, 2, ..., f. Return 
   the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll 
   the dice so the sum of the face up numbers equals target. [LeetCode:1155]"""
""" Write a recursive function diceRoll that accepts an integer representating a
    number of 6-sided dice to roll, and output all possible combinations of 
    values that could appear on the dice."""


def _test_dice_roll():
    n = randrange(0, 5)
    dice_roll(n)
    print('Number of Dice: ', n)


def _test_sum_dice_roll():
    dice = randrange(1, 5)
    target = randrange(1, 1 + dice * 6)

    res1 = sum_dice_roll(dice, target)
    res2 = Rec.sum_dice_roll(dice, target)
    assert res1 == res2
    print('Number of Dice: ', dice, 'Target: ', target)


""" Write a method to compute all permutations of a string. [CtCI: 9.5]. """


def permute_str_A(s: str) -> Container[Sequence]:
    """
    Args:
        s: The string to be permuted.
    """
    pass


def permute_str_B(s: str):
    pass


def permute_str_C(s: str):
    pass


def _test_permutation_str():
    s = 'RACE'
    res1 = permute_str_A(s)
    res2 = permute_str_B(s)
    res3 = permute_str_C(s)

    assert len(res1) == len(res2) == len(res3)
    for i, j, k in zip(res1, res2, reversed(res3)):
        print(i, j, k)


""" Write a program which takes as input an array of distinct integers and 
    generates all permutations of that array. No permutation of the array may 
    appear more than once. [EPI: 15.3]"""


def permutation_list_A(L):
    pass


def permutation_list_B(L):
    pass


def _test_permutation_list():
    L = list('1234')
    res1 = permutation_list_A(L)
    print(res1)
    res2 = permutation_list_B(L)
    for _ in res2:
        print(_)
    assert len(res1) == 24
    assert len(res2) == 24


""" Write a function that takes as input a set and returns its power set. 
    [EPI: 15.4]"""


def power_set(L):
    """ Computes the power set of the given set, L"""
    pass


def _test_power_set():
    shah = list("SHAH")
    res = power_set(shah)
    # assert len(res) == pow(2, len(shah))
    for item in res:
        print(item)


""" Write a program which computes all size k subsets of {1, 2, ..., n} where k 
    and n are program inputs.[EPI: 15.5]"""


def combinations(n, k):
    pass


def directed_combinations(offset, k, partial_combination, result):
    pass


# NOT WORKING PROPERLY  !!!


def comb_B(L, k):
    pass


def _comb_B(L, k, chosen, offset, result):
    pass


def _test_comb_B():
    L = list("EAT")
    people = ["Jane", "Bob", "Matt", "Sara", "Shah"]
    print_matrix(comb_B(people, 3))


""" Implement an algorithm to print all valid (i.e. properly opened and closed)
    combinations of n-pairs of parentheses. [CtCI: 9.6]"""


def gen_parenthesis1(n):
    result = []
    _gen_parenthesis1(n, n, result)
    return result


def _gen_parenthesis1(l, r, result, paren=[]):
    if not l and not r: result.append(tuple(paren))
    if not l or not r: return

    if l > 0:
        paren.append('(')
        _gen_parenthesis1(l - 1, r, result, paren)
        paren.pop()
    if r > l:
        paren.append(')')
        _gen_parenthesis1(l, r - 1, result, paren)
        result.pop()


def gen_parenthesis2(n):
    result = []
    _gen_parenthesis2(n, n, result)
    return result


def _gen_parenthesis2(l, r, result, parens=''):
    if not r: result.append(parens)
    if l > 0: _gen_parenthesis2(l - 1, r, result, parens + '(')
    if r > l: _gen_parenthesis2(l, r - 1, result, parens + ')')


def _test_gen_parenthesis():
    n = randint(3, 6)

    # res1 = gen_parenthesis1(n)
    res2 = gen_parenthesis2(n)
    print(res2)
    print('Number of parenthesis pair: ', n)


""" Write an algorithm to print all ways of arranging eight queens on an 8x8 
    chess board so that none of them share the same row, column or diagonal. 
	In this case, "diagonal" means all diagonals, not just the two that bisect 
    the board. [CtCI: 9.9]"""


def n_queens(num_of_queens) -> Container[list]:
    pass


def solve_n_queens(n):
    result = []
    _solve_n_queens(0, n, result, [0] * n)
    return result


def _solve_n_queens(row, n, result, columns):
    if row == n:
        # All queens are legally placed.
        result.append(tuple(columns))
        return None
    for col in range(n):
        # Test if a newly placed queen will conflict any earlier queens
        # placed before.
        L = [
            abs(c - col) not in (0, row - i)
            for i, c in enumerate(columns[:row])
        ]
        if all(L):
            columns[row] = col
            _solve_n_queens(row + 1, n, result, columns)


def _print_board(L):
    board = []
    for i in L:
        row = ['_'] * len(L)
        row[i] = 'Q'
        board.append(row)
    for i in board:
        print(i)
    print()


def _test_n_queens():
    random_int = randrange(3, 11)
    res1 = n_queens(random_int)
    res2 = solve_n_queens(random_int)
    assert res1 == res2
    for board in res1:
        _print_board(board)
    print('Number of Queens:', random_int, 'Number of ways:', len(res1))


""" Write a program which prints a sequence of operations that transfer n rings 
	from one peg to another. You have a third peg, which is initially empty. 
    The only operation you can perform is taking a single ring from the top of 
    the peg and placing it on the top of another peg. You must never place a 
    larger ring above a smaller ring. [EPI: 15.1]"""
""" A child is running up a staircase with n steps, and can hop either 1 step, 
    2 steps, or 3 steps at a time. Implement a method to count how many possible 
    ways the child can run up the stairs. [CtCI: 9.1]"""
""" Imagine a robot sitting on the upper left corner of an X by Y grid. The
    robot can only move in toward directions: right and down. How many possible 
    paths are there for the robot to go from (0,0) to (X,Y)?
    Imagine certain spots are "off limits" such that the robot cannot step on 
    them. Design an algorithm to find a path for the robot from the top left to 
    the bottom right.[CtCI: 9.2]"""
""" Check if array is sorted using recursion. """


def is_sorted(a, high):
    if high == 0:
        return True
    elif a[high - 1] <= a[high]:
        return is_sorted(a, high - 1)

    return False


""" Implement a function that verify if a given string is a Palindrom. """
""" Implement a function that compute exponent of a given base. """
""" Compute the n-th Fibonacci Number.	"""
""" Compute the n-th Factorial. """
""" Implement the Euclidean algorithm for calculating the greatest common 
    divisor of two numbers. [EPI: 15:boot camp].
"""

if __name__ == '__main__':
    # _test_print_binary()
    # _test_print_decimal()
    # _test_dice_roll()
    _test_sum_dice_roll()
    # _test_permutation_str()
    # _test_comb_B()
    # _test_permutation_list()
    # _test_power_set()
    # _test_gen_parenthesis()
    # _test_n_queens()
