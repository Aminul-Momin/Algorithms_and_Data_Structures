from random import randint
from math import floor, log2, ceil
from ads.searching._nodes import BSTNode
from ads.exercises.tree.height_bt import height_bt_v2
#==============================================================================
""" Create a BST with minimal height from a increasing order sorted array. """
#==============================================================================


def min_height_bst(L):
    def _min_height_bst(L, low, high):
        if low > high: return None
        mid = (low + high) // 2
        x = BSTNode(None, L[mid])
        x._left = _min_height_bst(L, low, mid - 1)
        x._right = _min_height_bst(L, mid + 1, high)
        return x

    return _min_height_bst(L, 0, len(L) - 1)


def _test_min_height_bst():
    for i in range(1):
        N = 15
        # N = randint(10, 30)
        L = sorted([randint(-20, 21) for i in range(N)], reverse=True)
        bst = min_height_bst(L)
        height = height_bt_v2(bst)

        print('Length of L: ', len(L), '\nHeight of built tree: ', height)
        print(floor(log2(len(L))), ceil(log2(len(L))))
        assert floor(log2(len(L))) <= height <= ceil(log2(len(L)))


def main():
    _test_min_height_bst()


if __name__ == '__main__':
    main()
