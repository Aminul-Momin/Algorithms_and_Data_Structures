from random import randint

from ads.utils import gen_bst
from ads.searching import BSTNode as Node

#==============================================================================
""" Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes'
values.

Example:
                   .9..
                  /    \
                  6     12
                 / \   / \
                2  7  9  18
                /\ /\ /\ /\

Postorder Traversal: [2, 7, 6, 9, 18, 12, 9]
"""
#==============================================================================


def postorder_rec(x: Node) -> None:
    def _postorder_rec(x: Node):
        if not x: return None
        _postorder_rec(x._left)
        _postorder_rec(x._right)
        postorder.append(x._key)

    postorder = []
    _postorder_rec(x)
    return postorder


def main():
    bst = gen_bst([randint(0, 20) for _ in range(7)])
    print(bst, postorder_rec(bst), sep='\n\n')


if __name__ == '__main__':
    main()
