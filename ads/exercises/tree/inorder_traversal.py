from collections import deque
from random import randint

from ads.utils import gen_bst
from ads.searching import BSTNode as Node
#==============================================================================
""" Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes'
values.
"""
#==============================================================================


def inorder_rec(x: Node) -> None:
    def _inorder_rec(x: Node):
        if not x: return None
        _inorder_rec(x._left)
        inorder.append(x._key)
        _inorder_rec(x._right)

    inorder = []
    _inorder_rec(x)
    return inorder


def main():
    bst = gen_bst([randint(0, 20) for _ in range(7)])
    print(bst, inorder_rec(bst), sep='\n\n')


if __name__ == '__main__':
    main()
