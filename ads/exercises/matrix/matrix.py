from random import randint, randrange

from ads.utils import print_matrix
#==============================================================================
""" Search in a 2D sorted array. - [EPI: 11.6, CtCI: 11.6].

    Given an MxN matrix in which each row and each column is sorted in
    ascending order, write a method to find an element.


"""


def matrix_search(A, x):

    row, col = 0, len(A[0]) - 1  # Start from the top-right corner.
    # Keeps searching while there are unclassified rows and columns.
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1  # Eliminate this row.
        else:  # A[row][col] > x.
            col -= 1  # Eliminate this column.
    return False


""" Given an image represented by an NxN(SQUARE) matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place? [CiCI: 1.6]. """


def rotate_matrix(M):
    for layer in range(len(M) // 2):
        first = layer
        last = (len(M)-1) - first

        for i in range(first, last):
            offset = i - first
            top = M[first][i]

            M[first][i] = M[last - offset][first]
            M[last - offset][first] = M[last][last - offset]
            M[last][last - offset] = M[i][last]
            M[i][last] = top


def test_rotate_matrix():
    N = randint(3, 6)
    M = [[randrange(0, 10) for i in range(N)] for i in range(N)]
    print_matrix(M)
    print()
    rotate_matrix(M)
    print_matrix(M)


""" Print a MxN Matrix Diagonally. """
""" Write a program that takes a NxN Matrix and return SPIRAL ORDERING of the Matrix. [EPI: Array: 5.18]. """
""" Write a method that takes a non-negative number n as input and return first n rows of the PASCAL'S TRIANGLE. - [EPI:Array: 5.20]. """
""" Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0. """
""" Write a method that takes 9x9 Matrix representing a partially completing SUDOKU as input and return whether it's valid or not. - [EPI: Array: 5.17]. """
""" Transpose a Matrix. """


def transpose_matrix():
    def transpose(M):
        T = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
        return T

    num_rows, num_cols = 5, 4
    M = [[randrange(1, 10) for j in range(num_cols)] for i in range(num_rows)]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], sep='', end=' ')
        print('')

    print('After transpose: ')
    M = transpose(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], sep='', end=' ')
        print('')


""" Multiply a matrix """


def matrix_mul(X, Y):
    result = [[] for i in range()]
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


if __name__ == "__main__":
    # test_rotate_matrix()
    transpose_matrix()
