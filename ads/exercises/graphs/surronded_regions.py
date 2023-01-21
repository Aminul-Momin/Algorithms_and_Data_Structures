from typing import List
#==============================================================================
"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

EXAMPLE 1:
    INPUT: board = [["X","X","X","X"],
                    ["X","O","O","X"],
                    ["X","X","O","X"],
                    ["X","O","X","X"]]
    
    OUTPUT: [["X","X","X","X"],
             ["X","X","X","X"],
             ["X","X","X","X"],
             ["X","O","X","X"]]
    
    EXPLANATION:
        Surrounded regions should not be on the border, which means that any
        'O' on the border of the board are not flipped to 'X'. Any 'O' that is
        not on the border and it is not connected to an 'O' on the border will
        be flipped to 'X'. Two cells are connected if they are adjacent cells
        connected horizontally or vertically.

EXAMPLE 2:
    INPUT: board = [["X"]]
    OUTPUT: [["X"]]

CONSTRAINTS:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.


"""
#==============================================================================


def solve(board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
        if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
            return
        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(ROWS):
        for c in range(COLS):
            if (board[r][c] == "O"
                    and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                capture(r, c)

    # 2. Capture surrounded regions (O -> X)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    # 3. Uncapture unsurrounded regions (T -> O)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"
