from random import randrange

def print_matrix_rec(M):
    counter = [0]
    _print_matrix_rec(M, len(M)-1, len(M[0])-1, counter)
    return counter[0]


def _print_matrix_rec(M, row, col, counter):
    counter[0] += 1
    if row < 0 or col < 0: return
    _print_matrix_rec(M, row-1, col, counter)
    _print_matrix_rec(M, row, col-1, counter)
    print(M[row][col])


def _test_print_matrix_rec():
    M = [[randrange(10, 100)]*5 for i in range(5)]
    for i in M: print(i)
    print(print_matrix_rec(M))

if __name__ == "__main__":
    _test_print_matrix_rec()
