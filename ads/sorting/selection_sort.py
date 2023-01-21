from ads.utils.utils import swap, is_sorted
from random import randrange


def selection_sort(L) -> None:
    """Sorts the given list using selection sort algorithm.

    Args:
        a (list): The list to be sorted
    """
    for i in range(len(L)):
        min_idx = i
        for idx in range(i, len(L)):
            if L[idx] < L[min_idx]:
                min_idx = idx
        swap(L, min_idx, i)


def main():
    L = [randrange(-99, 100) for _ in range(10)]
    assert not is_sorted(L)
    sorted_L = sorted(L)
    selection_sort(L)
    assert L == sorted_L


if __name__ == '__main__':
    main()
