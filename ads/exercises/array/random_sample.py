from random import sample, randint
"""Implement an algorithm that takes as imput an array of distinct elements and a size and returns a subset of the given size of the array elements. All subsets should be equally likely. Return the result in input array. itself. - [EPI: 5.12]. """


def random_sampling(k, A):

    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]


# Pythonic solution
def random_sampling_pythonic(k, A):
    A[:] = sample(A, k)
