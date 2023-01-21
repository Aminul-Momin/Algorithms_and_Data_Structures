from typing import List, Sequence
from random import randint, randrange
"""Imagine a robot sitting on the upper left corner of grid with r rows and c
   columns. The robot can only move in two directions, right and down, but
   certain cells are "off limits" such that the robot cannot step on them.
   Design an algorithm to find a path for the robot from the top left to the
   bottom right. {CtCI: 9.2}."""


#Solution with recursion O(2^r+c)
def get_path1(M):
    if M == None or len(M) == 0: return None
    path = []
    if _get_path1(M, len(M) - 1, len(M[0]) - 1, path): return path
    return None


def _get_path1(M, m, n, path):
    #if out of bounds or not available, return
    if n < 0 or m < 0 or not M[m][n]:
        return False

    isAtOrigin = (m == 0) and (n == 0)
    from_top = _get_path1(M, m - 1, n, path)
    from_left = _get_path1(M, m, n - 1, path)

    #if there's a path from the start to here, add my location
    if isAtOrigin or from_top or from_left:
        path.append((m, n))
        return True

    return False


def get_path2(M):
    if M == None or len(M) == 0: return None
    path = []
    if _get_path2(M, len(M) - 1, len(M[0]) - 1, path): return path
    return None


# NOT WORKING !!
def _get_path2(M, num_row, num_col, path):  # ANY ONE PATH
    if (num_row == 0) and (num_col == 0): return True

    sucess = False
    if num_row >= 1 and M[num_row - 1][num_col]:
        sucess = _get_path2(M, num_row - 1, num_col, path)

    if not sucess and num_col >= 1 and M[num_row][num_col - 1]:
        sucess = _get_path2(M, num_row, num_col - 1, path)

    #if there's a path from the start to here, add my location
    if sucess: path.append((num_row, num_col))

    return sucess


#Solution with memoization


def get_pathMemoized(M):
    if M == None or len(M) == 0: return None
    path = []
    failedPoints = []
    if isPathMemoized(M, len(M) - 1, len(M[0]) - 1, path, failedPoints):
        return path
    return None


def isPathMemoized(M, row, col, path, failedPoints):
    #If out of bounds or not availabe, return
    if col < 0 or row < 0 or not M[row][col]:
        return False

    point = (row, col)

    # if we've already visisted this cell, return
    if point in failedPoints:
        return False

    isAtOrigin = (row == 0) and (col == 0)
    from_top = isPathMemoized(M, row - 1, col, path, failedPoints)
    from_left = isPathMemoized(M, row, col - 1, path, failedPoints)

    #If there's a path from start to my current location, add my location
    if isAtOrigin or from_left or from_top:
        path.append(point)
        return True

    failedPoints.append(point)
    return False


def _test_path():
    m, n = randint(2, 10), randint(2, 10)
    M1 = [[True] * m for _ in range(n)]
    M2 = [[True] * m for _ in range(n)]
    before = get_path1(M1)
    print(before)
    assert before == get_pathMemoized(M2) != get_path2(M2)

    for _ in range(len(M1)):
        r, c = randrange(0, len(M1) - 1), randrange(0, len(M1[0]) - 1)
        M1[r][c], M2[r][c] = False, False

    assert get_path1(M1) != before
    print(get_path1(M1))
    for i in M1:
        print(i)


# TakenFrom: https://leetcode.com/problems/unique-paths-ii/solution/
def uniquePathsWithObstacles(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    m = len(M)
    n = len(M[0])

    # If the starting cell has an obstacle, then simply return as there would be
    # no paths to the destination.
    if M[0][0] == 1:
        return 0

    # Number of ways of reaching the starting cell = 1.
    M[0][0] = 1

    # Filling the values for the first column
    for i in range(1, m):
        M[i][0] = int(M[i][0] == 0 and M[i - 1][0] == 1)

    # Filling the values for the first row
    for j in range(1, n):
        M[0][j] = int(M[0][j] == 0 and M[0][j - 1] == 1)

    # Starting from cell(1,1) fill up the values
    # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
    # i.e. From above and left.
    for i in range(1, m):
        for j in range(1, n):
            if M[i][j] == 0:
                M[i][j] = M[i - 1][j] + M[i][j - 1]
            else:
                M[i][j] = 0

    # Return value stored in rightmost bottommost cell. That is the destination.
    return M[m - 1][n - 1]


if __name__ == "__main__":
    _test_path()
