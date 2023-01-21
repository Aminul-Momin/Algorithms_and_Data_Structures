from ads.utils import is_sorted
from random import randrange


def bubble_sort(L):
    for j in range(len(L)):
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp


def main():
    L = [randrange(-99, 100) for _ in range(10)]
    assert not is_sorted(L)
    sorted_L = sorted(L)
    bubble_sort(L)
    assert L == sorted_L


if __name__ == '__main__':
    main()
