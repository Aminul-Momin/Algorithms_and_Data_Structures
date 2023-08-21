
from ads.utils import swap

def cyclic_sort(a):
    N = len(a)
    i = 0
    while i < N:
        if a[i] == i+1: i = i+1
        else: swap(a, i, a[i]-1)

def test_cyclic_sort():
    for _ in range(1000):
        from numpy import random as r
        P = list(r.permutation(10)+1)
        try:
            expected = sorted(P)
            print(P, expected)
            cyclic_sort(P)
            assert P == expected
        except:
            print(f"""
                Given: {P},
                Expected: {expected}""")
            break


# ================================================================


if __name__ == '__main__':
    test_cyclic_sort()
