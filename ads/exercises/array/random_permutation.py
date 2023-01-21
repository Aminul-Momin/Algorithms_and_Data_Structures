from ads.exercises.array.random_sample import *
from random import randint
"""Write a program that creates uniformly random permutations of {0,1, .., n-1} You are given a random number generator that returns integer in the set {0, 1, ... n-1} with equal probability. use as few calls to it as possible. - [EPI: 5.14] [CtCI:18.2]. """


def compute_random_permutation(n):

    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation


def main():
    n = randint(0, 10)
    print(n)


if __name__ == '__main__':
    main()
