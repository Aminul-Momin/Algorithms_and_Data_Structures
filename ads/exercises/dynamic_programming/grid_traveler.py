#==============================================================================
#==============================================================================
"""
Imagine a robot sitting on the upper left corner of an X by Ygrid. The robot
can only move in two directions: right and down.

How many possible paths are there for the robot to go from (0, 0) to (X, Y) ?

Imagine certain spots are "off limits," such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the
bottom right. - [EPI: 16.3, CtCI: 9.2].

1) Write a function 'grid_traveler(m, n)' that calculates the number of paths.
2) Write a function 'find_path(m, n)' that finds tha actual paths.

Examples:
    1. grid_traveler((0, 0)) -> 0
    2. grid_traveler((1, 1)) -> 1
    3. grid_traveler((2, 3)) -> 3
    4. grid_traveler((3, 2)) -> 3
    5. grid_traveler((3, 3)) -> 6
    6. grid_traveler((13, 13)) -> 2704156

"""
#==============================================================================
from random import randint, randrange
from itertools import accumulate
from functools import lru_cache

from ads.utils import *


#==============================================================================
@ lru_cache(None)
def grid_traveler_rec(m: int, n: int) -> int:
    """Computes the number of ways of traveling from source to destination.

    Args:
        m: The total vertical distance.
        n: The total horizontal distance.

    Returns:
        The number of ways ways you can travel to the goal on a grid
        with dimensions (m x n).
    """

    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return grid_traveler_rec(m - 1, n) + grid_traveler_rec(m, n - 1)


@lru_cache(None)
def grid_traveler_rec_v2(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    from_top = grid_traveler_rec_v2(m - 1, n)
    from_left = grid_traveler_rec_v2(m, n - 1)
    return from_top + from_left


def grid_traveler_memo(m: int, n: int, memo={}) -> int:
    """Computes the number of ways of traveling from source to destination.

    Args:
        m: The total vertical distance.
        n: The total horizontal distance.

    Returns:
        The number of ways ways you can travel to the goal on a grid
        with dimensions (m x n).
    """

    key = f"{m},{n}"  # make sure (12 x 1) != (1 x 21) by using comma
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    memo[key] = grid_traveler_memo(m - 1, n) + grid_traveler_memo(m, n - 1)
    return memo[key]


def grid_traveler_memo_v2(m, n):

    # It generate error if `M` (matrix) is EMPTY
    def _grid_traveler_memo_v_2a(m, n, M):
        if m == n == 0: return 1

        if M[m][n] == 0:
            from_top = 0 if m == 0 else _grid_traveler_memo_v_2a(m - 1, n, M)
            from_left = 0 if n == 0 else _grid_traveler_memo_v_2a(m, n - 1, M)

            M[m][n] = from_top + from_left

        return M[m][n]

    def _grid_traveler_memo_v_2b(m, n, M):
        if m == n == 0: return 1
        if m < 0 or n < 0: return 0

        if M[m][n] == 0:
            from_top = _grid_traveler_memo_v_2b(m - 1, n, M)
            from_left = _grid_traveler_memo_v_2b(m, n - 1, M)

            M[m][n] = from_top + from_left

        return M[m][n]

    def _grid_traveler_memo_v_2c(m, n, memo={}):
        key = f"{m},{n}"
        if key in memo: return memo[key]
        if m == n == 0: return 1
        if m < 0 or n < 0: return 0

        from_top = _grid_traveler_memo_v_2c(m - 1, n, memo)
        from_left = _grid_traveler_memo_v_2c(m, n - 1, memo)

        memo[key] = from_top + from_left

        return memo[key]

    M = [[0] * n for _ in range(m)]
    return _grid_traveler_memo_v_2c(m - 1, n - 1)

def count_paths(grid):
    """
    - r = # rows
    - c = # columns
    - Time: O(r*c)
    - Space: O(r*c)
    """

    def _count_paths(grid, r, c, memo):
        pos = (r, c)
        if pos in memo: return memo[pos]

        if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X': return 0

        if r == len(grid) - 1 and c == len(grid[0]) - 1: return 1

        memo[pos] = _count_paths(grid, r + 1, c, memo) + _count_paths(grid, r, c + 1, memo)
        return memo[pos]

    return _count_paths(grid, 0, 0, {})


def grid_traveler_tbl(m: int, n: int) -> int:
    """Computes the number of ways of traveling from source to destination.

    Args:
        m: The total vertical distance.
        n: The total horizontal distance.

    Returns:
        The number of ways ways you can travel to the goal on a grid
        with dimensions (m x n).
    """

    if m == 0 or n == 0: return 0

    tbl = [[0] * (n + 1) for _ in range(m + 1)]
    tbl[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if (j + 1) <= n: tbl[i][j + 1] += tbl[i][j]
            if (i + 1) <= m: tbl[i + 1][j] += tbl[i][j]

    return tbl[m][n]


def grid_traveler_tbl_v2(m, n):
    M = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0: M[i][j] = 1
            else: M[i][j] = M[i - 1][j] + M[i][j - 1]

    return M[m - 1][n - 1]


def grid_traveler_tbl_v3(m, n):

    if m < n: m, n = n, m

    A = [1] * n
    for _ in range(1, m):
        prev_res = 0
        for j in range(n):
            A[j] += prev_res
            prev_res = A[j]
    return A[n - 1]


# Pythonic implementation of space efficient 'number_of_ways'.
def grid_traveler_tbl_v3_pythonic(n, m):
    if n < m: n, m = m, n
    A = [1] * m
    for _ in range(1, n):
        A = list(accumulate(A))
    return A[-1]


#==============================================================================
#==============================================================================
"""
Imagine certain spots are "off limits", such that the robot cannot step on
them. Design an algorithm to find `a path` for the robot from the top left to the
bottom right. - [EPI: 16.3, CtCI: 9.2].
"""

#==============================================================================
def find_path_memo(M):
    """Find a path from lower-right to upper-left of a `m` by `n` grid.

    Args:
        M : the `m` by `n` grid with obstacles
    Returns
        (list): Collection of points on the given grid.
    """
    def _find_path_memo(m, n, M, chosen, failed_point_memo={}):
        key = f"{m},{n}"
        if key in failed_point_memo: return False
        if m == 0 and n == 0: return [(0, 0)]
        if m < 0 or n < 0 or not M[m][n]: return False

        from_top = _find_path_memo(m - 1, n, M, chosen, failed_point_memo)
        if from_top is not False: return from_top + [(m, n)]

        from_left = _find_path_memo(m, n - 1, M, chosen, failed_point_memo)
        if from_left is not False: return from_left + [(m, n)]

        # Cache the failed point so that it is not tried second time.
        failed_point_memo[key] = False
        return failed_point_memo[key]

    if not M or len(M) == 0: return None
    m, n = len(M), len(M[0])
    return _find_path_memo(m - 1, n - 1, M, chosen=[])


def collect_paths(M):
    """Collece all the paths from lower-right to upper-left of a `m` by `n` grid.

    Args:
        M : the `m` by `n` grid with/without obstacles
    Returns
        (list): Collection of path from lower-right to upper-left.
    """
    def _collect_paths(m, n, M, result, chosen):
        if not M[m][n]: return None
        if m < 0 or n < 0: return None

        chosen.append((m, n))
        if m == 0 and n == 0: result.append([*chosen, (0, 0)])

        from_top = _collect_paths(m - 1, n, M, result, chosen)
        from_left = _collect_paths(m, n - 1, M, result, chosen)
        chosen.pop()

    m, n = len(M), len(M[0])
    result = []
    _collect_paths(m - 1, n - 1, M, result, [])
    return result



def _test_collect_paths():

    m, n = randrange(1, 9), randrange(1, 9)

    M = [[True] * n for _ in range(m)]
    N = len(M) + len(M[0])

    for _ in range(N):
        r, c = randrange(0, len(M) - 1), randrange(0, len(M[0]) - 1)
        M[r][c] = False

    M[0][0], M[m - 1][n - 1] = True, True

    paths1 = collect_paths(M)
    print_matrix(paths1)
    #print_matrix(M)


def _test_grid_traveler():
    m, n = randint(3, 10), randint(3, 10)
    # m, n = 4, 7
    num_ways_memo = grid_traveler_memo(m, n)
    num_ways_memo_v2 = grid_traveler_memo_v2(m, n)
    num_ways_tbl = grid_traveler_tbl(m, n)
    num_ways_tbl_v2 = grid_traveler_tbl_v2(m, n)
    num_ways_tbl_v3 = grid_traveler_tbl_v3(m, n)
    num_ways_tbl_pythonic = grid_traveler_tbl_v3_pythonic(m, n)
    num_ways_rec = grid_traveler_rec(m, n)
    num_ways_rec_v2 = grid_traveler_rec_v2(m, n)

    assert num_ways_memo == num_ways_memo_v2 == num_ways_tbl_v2
    assert num_ways_tbl_v3 == num_ways_tbl_pythonic == num_ways_rec
    assert num_ways_tbl_v2 == num_ways_tbl_v3 == num_ways_tbl

    assert num_ways_rec == num_ways_rec_v2  # ??????????


if __name__ == '__main__':
    _test_grid_traveler()
