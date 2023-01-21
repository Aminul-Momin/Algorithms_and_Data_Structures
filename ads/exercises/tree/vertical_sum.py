from ads.searching.bst import AVL
from random import randint
from typing import Dict

from ads.searching import BSTNode as Node
from ads.utils import gen_bst
#==============================================================================
""" Print the Vertical Sum in binary Tree. """
#==============================================================================


def vertical_sum(x):
    ht = {}
    _vertical_sum(x, ht, 0)
    return ht


def _vertical_sum(x: Node, ht: Dict[int, int], hd: int):
    '''
    args:
        x : A binary tree.
        ht: a hash table.
        hd: horizontal distance
    '''
    if not x: return None
    _vertical_sum(x._left, ht, hd - 1)
    ht[hd] = ht.get(hd, 0) + x._key

    # if ht.get(hd) is None: ht[hd] = x._key
    # else: ht[hd] = ht.get(hd) + x._key

    _vertical_sum(x._right, ht, hd + 1)


def main():
    L = [randint(0, 20) for _ in range(16)]
    bst = gen_bst(L, type=AVL)
    print(bst)
    d = vertical_sum(bst)
    for item in d.items():
        print(item)


if __name__ == '__main__':
    main()
