from typing import Container
""" Enumerates all the primes upto n. [EPI: 5.9].

    Examples:
        generate_primes(0)  -> []
        generate_primes(2)  -> [2]
        generate_primes(4)  -> [2, 3]
        generate_primes(6)  -> [2, 3, 5]
        generate_primes(8)  -> [2, 3, 5, 7]
        generate_primes(10) -> [2, 3, 5, 7]
        generate_primes(12) -> [2, 3, 5, 7, 11]
        generate_primes(14) -> [2, 3, 5, 7, 11, 13]

"""


def generate_primes_v1(n: int) -> Container[int]:
    """Computes and returns all the primes up to 'n'.

    Args:
        n: The integer upto which all primes to be computed.

    Returns:
        All the primes upto 'n'.
    """

    primes = []
    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for p in range(2 * i, n + 1, i):
                is_prime[p] = False

    return primes


def generate_primes_v2(n: int) -> Container[int]:
    """Computes and returns all the primes up to 'n'.

    Args:
        n: The integer upto which all primes to be computed.

    Returns:
        All the primes upto 'n'.
    """

    if n < 2:
        return []
    size = (n - 3) // 2 + 1

    # Stores the primes from 1 to n.
    primes = [2]

    # is_prime[i] represents (2i + 3) is prime or not.
    # Initially set each to true. Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)

            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes
