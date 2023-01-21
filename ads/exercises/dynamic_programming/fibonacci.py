"""
Write a function 'fib(n)' that takes in a number as an argument. The function
should return the n-th number of the Fibonacci sequence.

The 0th number of the sequence is 0.
The 1st number of the sequence is 1.

To generate the next number of the sequence, we sum the previous two.

Examples:
    fib(0) -> 0
    fib(1) -> 1
    fib(2) -> 1
    fib(3) -> 2
    fib(4) -> 3
    fib(5) -> 5
    fib(6) -> 8
    fib(7) -> 13
    fib(8) -> 21
    fib(9) -> 34
"""

def fib_rec(n: int) -> int:
    """Computes the n-th Fibonacci number.

    Args:
        n: The number of which Fibonacci sequence to be computed.

    Returns:
        The n-th number of the Fibonacci sequence.
    """
    if n <= 1: return n
    else: return fib_rec(n-1) + fib_rec(n-2)

def fib_dp_tbl(n: int) -> int:
    """Computes the n-th Fibonacci number.

    Args:
        n: The number of which Fibonacci sequence to be computed.

    Returns:
        The n-th number of the Fibonacci sequence.
    """
    memo = {0: 0, 1: 1}
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fib_dp_memo(n: int, memo: dict ={0: 0, 1: 1}):
    """Computes the n-th Fibonacci number.

    Args:
        n: The number of which Fibonacci sequence to be computed.

    Returns:
        The n-th number of the Fibonacci sequence.
    """
    if n not in memo:
        memo[n] = fib_dp_memo(n-1, memo) + fib_dp_memo(n-2, memo)
    return memo[n]
