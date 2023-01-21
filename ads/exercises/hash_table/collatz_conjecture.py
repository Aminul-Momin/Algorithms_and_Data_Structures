""" Test the Collatz conjecture. - [EPI:12.11]

The Collatz conjecture is the following: Take any natural number. If it is
odd, triple it and add one; if it is even, halve it. Repeat the process
indefinitely. No matter what number you begin with, you will eventually
arrive at 1. As an example, if we start with 11, we get the sequence 11, 34,
17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. Despite intense efforts, the
Collatz conjecture has not been proved or disproved. Suppose you were given
the task of checking the Collatz conjecture for the first billion integers.A
direct approach would be to compute the convergence sequence for each number
in this set.Test the Collatz conjecture for the first n positive integers.

Hint: How would you efficiently check the conjecture for n assuming it holds
for all m < n?
"""


def test_collatz_conjecture(n):

    # Stores odd numbers already tested to converge to 1.
    verified_numbers = set()

    # Starts from 3, hypothesis holds trivially for 1.
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                # We previously encountered test_i, so the Collatz sequence has
                # fallen into a loop. This disproves the hypothesis, so we
                # short-circuit, returning False.
                return False
            sequence.add(test_i)

            if test_i % 2:  # Odd number.
                if test_i in verified_numbers:
                    break  # test_i has already been verified to converge to 1.
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1  # Multiply by 3 and add 1.
            else:
                test_i //= 2  # Even number, halve it.
    return True


def main():
    pass


if __name__ == '__main__':
    main()