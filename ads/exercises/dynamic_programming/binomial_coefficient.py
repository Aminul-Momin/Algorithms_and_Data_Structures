from random import randint
from ads.utils import print_matrix
#==============================================================================
#==============================================================================
""" Computes the binomial coefficients. - [EPI: 16.4]. """


def binomial_coef(n, k):
    """Computes the k-th coefficient of n-th degree binomial.

    Args:
        n (int): The degree of binomial.
        k (int): The order of binomial coefficient.

    Returns:
        (int): The k-th coefficient of n-th degree binomial.
    """
    def compute_tbl(n, k, C):
        """Build the table of binomial coefficients .

        Args:
            n (int): The degree of binomial.
            k (int): The order of binomial coefficient.
            C (List[List[int]]): The table of binomial coefficient.

        Returns:
            (int): The k-th coefficient of n-th degree binomial.
        """
        if k in (0, n): return 1
        if C[n][k] == 0:
            # C(i, j) = C(i - 1, j) + C(i - 1, j - 1).
            C[n][k] = compute_tbl(n - 1, k, C) + compute_tbl(n - 1, k - 1, C)

        return C[n][k]

    tbl = [[0] * (k + 1) for _ in range(n + 1)]
    return compute_tbl(n, k, tbl)


def binomial_coef_v2(n, k):
    """Computes the k-th coefficient of n-th degree binomial.

    Args:
        n (int): The degree of binomial.
        k (int): The order of binomial coefficient.

    Returns:
        (int): The k-th coefficient of n-th degree binomial.
    """
    tbl = [[0] * (k + 1) for _ in range(n + 1)]
    num_row, num_col = len(tbl), len(tbl[0])

    for i in range(num_row):
        for j in range(num_col):

            if j == 0 or i == j: tbl[i][j] = 1
            else: tbl[i][j] = tbl[i - 1][j] + tbl[i - 1][j - 1]
    return tbl[-1][-1]


# Space efficient implementation.
def binomial_coef_v3(n, k):
    """Computes the k-th coefficient of n-th degree binomial.

    Args:
        n (int): The degree of binomial.
        k (int): The order of binomial coefficient.

    Returns:
        (int): The k-th coefficient of n-th degree binomial.
    """

    k = min(k, n - k)
    table = [1] + [0] * k
    # C(i, j) = C(i - 1, j) + C(i - 1, j - 1).
    for i in range(1, n + 1):
        for j in reversed(range(1, min(i, k) + 1)):
            table[j] = table[j] + table[j - 1]
    return table[-1]


def main():
    for _ in range(50):
        n = randint(0, 50)
        k = randint(0, n)

        bc1 = binomial_coef(n, k)
        bc2 = binomial_coef_v2(n, k)
        bc3 = binomial_coef_v3(n, k)
        assert bc1 == bc2 == bc3
        print(bc1, bc2, bc3, sep='\t')


if __name__ == '__main__':
    main()
