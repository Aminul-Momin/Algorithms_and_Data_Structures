from functools import reduce
#==============================================================================
""" Smallest nonconstructible value. - [EPI:13.5]. """


def smallest_nonconstructible_value(A):

    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1: break
        max_constructible_value += a
    return max_constructible_value + 1


def smallest_nonconstructible_value_pythonic(A):
    func = lambda max_val, a: max_val + (0 if a > max_val + 1 else a)
    return reduce(func, sorted(A), 0) + 1


def main():
    pass


if __name__ == '__main__':
    main()