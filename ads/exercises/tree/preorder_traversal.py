from random import randint

from ads.utils import gen_bst
from ads.searching import BSTNode as Node

#==============================================================================
""" Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes'
values.
"""
#==============================================================================


def preorder_rec(x: Node) -> None:
    def _preorder_rec(x: Node):
        if not x: return None
        preorder.append(x._key)
        _preorder_rec(x._left)
        _preorder_rec(x._right)

    preorder = []
    _preorder_rec(x)
    return preorder


def main():
    bst = gen_bst([randint(0, 20) for _ in range(7)])
    print(bst, preorder_rec(bst), sep='\n\n')


if __name__ == '__main__':
    main()
