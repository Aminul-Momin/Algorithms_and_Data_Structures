from ads.utils.utils import green, red, yellow
from random import randint, randrange
from collections import namedtuple
from typing import List
from time import sleep
#==============================================================================
""" Knapsack 0/1
Write a program for the knapsack problem that selects a subset of items
that has maximum value and stisfies the weight constraint. All items have
integer weights and values. Return the value of the subset. - [EPI:16.6].
"""

#==============================================================================


# HAVE NOT PASSED THE TEST !!
def knapsack_memo(items: List[tuple], capacity: int):
    def _KN(r: int, c: int, L: List, M: List[List]):
        if r <= 0 or c <= 0: return 0
        elif M[r][c] == -1:
            _without = _KN(r - 1, c, L, M)
            _with = L[r - 1][1] + _KN(r - 1, c - L[r - 1][0], L,
                                      M) if c >= L[r - 1][0] else _KN(
                                          r - 1, c, L, M)
            M[r][c] = max(_without, _with)

        return M[r][c]

    M = [[-1] * (capacity + 1) for _ in range(len(items) + 1)]
    R, C = len(M) - 1, len(M[0]) - 1

    optimum_value = _KN(R, C, items, M)
    # for i in M: print(i)
    return optimum_value


# STILL HAVE A UNDETECTED BUG !!
def knapsack_tbl(L: List[tuple], cap: int):
    tbl = [[0] * (cap + 1) for _ in range(len(L) + 1)]
    T, C = len(tbl), len(tbl[0])

    for i in range(T):
        for j in range(C):
            if i + 1 < T and j < L[i][0]: tbl[i + 1][j] = tbl[i][j]
            if i + 1 < T and j + L[i][0] < C:
                max_profit = max(L[i][1] + tbl[i][j], tbl[i][j + L[i][0]])
                tbl[i + 1][j + L[i][0]] = max_profit

    return tbl[-1][-1]


def knapsack_tbl_v2(L, cap):
    M = [[0] * (cap + 1) for x in range(len(L) + 1)]

    for i in range(1, len(L) + 1):  # (i-1) --> index of i-th item
        for w in range(1, cap + 1):  # w --> weight
            item = L[i - 1]  # L[i-1] --> i-th item
            if w >= item.weight:
                _without = M[i - 1][w]
                _with = item.value + M[i - 1][w - item.weight]
                M[i][w] = max(_with, _without)
            else:
                M[i][w] = M[i - 1][w]

    return M[-1][-1]


def knapsack_tbl_v3(L, cap):
    M = [[0] * (cap + 1) for x in range(len(L) + 1)]
    L = [(0, 0)] + L

    for i, row in zip(range(1, len(L) + 1), M[1:]):
        for w, val in zip(range(1, len(row)), row[1:]):
            if w >= L[i].weight:
                _without = M[i - 1][w]
                _with = L[i].value + M[i - 1][w - L[i].weight]
                M[i][w] = max(_with, _without)
            else:
                M[i][w] = M[i - 1][w]

    return M[-1][-1]


def knapsack_rec(items, capacity):
    def _knapsack_rec(L, row, col):
        """
        Args:
            row: index of the list containing the items. (0 ≤ row ≤ len(L)-1)
            col: Capacity of the knapsack. (col ≥ 0)
        """
        if row < 0 or col == 0: return 0
        if col < L[row][0]: return _knapsack_rec(L, row - 1, col)
        else:
            _with = L[row][1] + _knapsack_rec(L, row - 1, col - L[row][0])
            _without = _knapsack_rec(L, row - 1, col)
            return max(_with, _without)

    return _knapsack_rec(items, len(items) - 1, capacity)


# taken from: CS Dojo <- Youtube
def knapsack_rec_v2(num_items: int, capacity: int, W: list, V: list):
    def _knapsack_rec_v2(n: int, c: int):
        """
        Args:
            n: number of items. (0 ≤ n ≤ len(W))
            c: Capacity of the knapsack. (c ≥ 0)
        """
        if n == 0 or c == 0: result = 0
        elif W[n - 1] > c: result = _knapsack_rec_v2(n - 1, c)
        else:
            _without = _knapsack_rec_v2(n - 1, c)
            _with = V[n - 1] + _knapsack_rec_v2(n - 1, c - W[n - 1])
            result = max(_without, _with)
        return result

    return _knapsack_rec_v2(num_items, capacity)


def _test_knapsack():

    Item = namedtuple('Item', ('weight', 'value'))
    functions = [knapsack_tbl, knapsack_tbl_v2, knapsack_rec, knapsack_rec_v2]
    # functions = [knapsack_tbl]

    for f in functions:
        for _ in range(1):

            items, items_named, weights, values = [], [], [], []
            N = randint(0, 50)
            for _ in range(N):
                w, v = randrange(0, 10), randrange(1, 30)
                weights.append(w)
                values.append(v)
                items.append((w, v))
                items_named.append(Item(w, v))

            # items = [(1, 4), (1, 5), (3, 3), (5, 4), (2, 10), (7, 6)]
            # items_named = [
            #     Item(1, 4),
            #     Item(1, 5),
            #     Item(3, 3),
            #     Item(5, 4),
            #     Item(2, 10),
            #     Item(7, 6)
            # ]

            # capacity = randint(10, 50)
            capacity = 7
            returned = None
            if f.__name__ == 'knapsack_tbl': returned = f(items, capacity)
            if f.__name__ == 'knapsack_tbl_v2':
                returned = f(items_named, capacity)
            if f.__name__ == 'knapsack_tbl_v3':
                returned = f(items_named, capacity)
            if f.__name__ == 'knapsack_memo': returned = f(items, capacity)
            if f.__name__ == 'knapsack_rec': returned = f(items, capacity)
            if f.__name__ == 'knapsack_rec_v2':
                returned = f(len(weights), capacity, weights, values)

            kn_tbl = knapsack_tbl_v2(items_named, capacity)

            try:
                assert kn_tbl == returned
            except (AssertionError):
                print(f"{yellow(f.__name__)} failed")
                print(f"Actual: {kn_tbl}, {yellow('Returned')} :{returned}")
                # print(weights, values, capacity)


def main():
    _test_knapsack()


if __name__ == '__main__':
    main()
