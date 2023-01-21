from random import randint
from ads.utils import *
#==============================================================================
"""
Given a black and white image (grid of 1 (blace) and 0 (white) pixel), Write a
function `remove_islands(grid)` that removes the black portions (black pixels)
of the given image that are not on the border of the image.
NOTE:
- Black pixel those are not on the border of the image are considered as island.

- Example:
    - remove_islands([]) ->
    - remove_islands([]) ->

"""
#==============================================================================


def gen_key(i, j):
    return "{}{}".format(i, j)


def is_border(i, j, M):
    if i == 0 or i == len(M) - 1 or j == 0 or j == len(M[0]) - 1:
        return True
    return False


def is_valid_index(i, j, M):
    valid_row_idx = 0 <= i <= len(M) - 1
    valid_col_idx = 0 <= j <= len(M[0]) - 1

    return valid_col_idx and valid_row_idx


def dfs_visit(i, j, M, border_islands):
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for (x, y) in steps:
        new_i = i + x
        new_j = j + y
        if not is_valid_index(new_i, new_j, M): continue

        neigh = M[new_i][new_j]
        key = gen_key(new_i, new_j)
        if neigh:
            border_islands[key] = True
            if not (key in border_islands):
                dfs_visit(new_i, new_j, M, border_islands)


def removes_island(M):
    border_islands = {}

    for i, row in enumerate(M):
        for j, val in enumerate(row):
            if val == 1 and is_border(i, j, M):
                border_islands[gen_key(i, j)] = True
                dfs_visit(i, j, M, border_islands)

    for i, row in enumerate(M):
        for j, val in enumerate(row):
            if val == 1 and not (gen_key(i, j) in border_islands):
                M[i][j] = 0
    return M


#==============================================================================
# Counts the numper of islands in a grid of 1s, 0s
#==============================================================================


def count_island(M):
    def bfs_visit(i, j, M):
        if is_valid_index(i, j, M):
            M[i][j] = 0
            bfs_visit(i, j + 1, M)
            bfs_visit(i, j - 1, M)
            bfs_visit(i + 1, j, M)
            bfs_visit(i - 1, j, M)

    count = 0
    for i, row in enumerate(M):
        for j, val in enumerate(row):
            if val == 1:
                count = +1
                bfs_visit(M, i, j)
    return count


def main():
    M_SIZE = 7
    M = [[randint(0, 1) for _ in range(M_SIZE)] for _ in range(M_SIZE)]

    # print_matrix(M)
    removes_island(M)
    print_matrix(M)


if __name__ == '__main__':
    main()
