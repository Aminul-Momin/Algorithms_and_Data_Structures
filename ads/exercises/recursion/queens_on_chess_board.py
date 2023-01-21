from random import randrange
#==============================================================================
"""
Write an algorithm to print all ways of arranging eight queens on an 8x8
chess board so that none of them share the same row, column or diagonal. In
this case, "diagonal" means all diagonals, not just the two that bisect the
board. - [CtCI: 9.9].
"""


def n_queens(n):
    def _n_queens(row, col, results, columns=[]):
        if row == col:
            results.append(tuple(columns))
            return None
        for c in range(col):
            columns.append(c)
            if is_valid(columns):
                _n_queens(row + 1, col, results, columns)
            columns.pop()

    def is_valid(L):
        row_id = len(L) - 1
        for i in range(row_id):
            col_diff = abs(L[row_id] - L[i])
            row_diff = row_id - i
            horizontal_attack = col_diff == 0
            diagonal_attack = col_diff == row_diff
            if horizontal_attack or diagonal_attack: return False

        return True

    results = []
    _n_queens(0, n, results)
    return results


def solve_n_queens(n):
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

    result = []
    _solve_n_queens(0, n, result, [0] * n)
    return result


def main():
    def _print_board(L):
        board = []
        for i in L:
            row = ['_*_'] * len(L)
            row[i] = '_Q_'
            board.append(row)
        for i in board:
            print(i)
        print()

    random_int = randrange(3, 11)
    res1 = n_queens(random_int)
    res2 = solve_n_queens(random_int)
    assert res1 == res2
    for board in res1:
        _print_board(board)
    print('Number of Queens:', random_int, 'Number of ways:', len(res1))


if __name__ == '__main__':
    main()
