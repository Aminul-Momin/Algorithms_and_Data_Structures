""" This is the Document string of this module"""
from random import randint
import sys
from typing import List
import logging
from ads.utils.utils import BASE_DIR


def logging_main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S',
        filename=BASE_DIR/"logs/root_logs.log",
        filemode="w"
    )

def merge_sort_v2(a: List) -> None:
    """Sorts the  specified list using merge-sort algorithm.

    Args:
        a: the list to be sorted
    """
    def _merge_sort_v2(a: List, low: int, high: int) -> None:


        def merge_v2(a: List, low: int, mid: int, high: int):

            print(_merge_sort_v2.__dict__)

            aux = [item for item in a]
            left, right, i = low, mid + 1, low

            while left <= mid and right <= high:
                if aux[left] <= aux[right]:  # ensures stability
                    a[i] = aux[left]
                    left += 1
                    i += 1
                else:
                    a[i] = aux[right]
                    right += 1
                    i += 1

            while left <= mid:
                a[i] = aux[left]
                i += 1
                left += 1


        if low >= high: return
        mid = (low + high) // 2

        # sorts first half of the array, a[low ... mid]
        _merge_sort_v2(a, low, mid)

        # sorts first half of the array, a[mid+1 ... high]
        _merge_sort_v2(a, mid + 1, high)

        # merges a[low ... mid] and a[mid+1 ... high], two halves of the array
        merge_v2(a, low, mid, high)

    _merge_sort_v2(a, 0, len(a) - 1)

def main():
    # print(sys.argv[1])
    print(__name__)
    print(__file__)
    print(__doc__)
    print(type(__builtins__))
    print(type(__package__))


if __name__ == "__main__":

    L = [randint(-10, 11) for _ in range(5)]
    print(L)
    merge_sort_v2(L)
    print(L)