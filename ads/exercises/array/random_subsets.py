from random import randrange
import random

"""Write a progra that takes as input a positive integer n and a size k <= n, and returns a size-k subset of {0, 1, 2, ..., n-1}. The subset should be represented as an array. All subset should be equally likely and, in addition, all permutations of elements of the array should be equally likely. [EPI: 5.15]. """

"""Write a method to shuffle a deck of cards. It must be a perfect shuffle, in other words, each of the 52! permutations has to be equally likely. Assume that you are given a perfect random number generator.[CtCI:18.2]. """


def random_subset(n, k):

    changed_elements = {}
    for i in range(k):
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]


# Pythonic solution
def random_subset_pythonic(n, k):
    return random.sample(range(n), k)
