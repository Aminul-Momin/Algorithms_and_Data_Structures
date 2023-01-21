from ads.searching import BSTNode, AVL
from random import randrange

from ads.utils import gen_bst

#==============================================================================
""" Check if the given tree is sum tree.

Write a function that returns true if the given Binary Tree is SumTree else
false. A SumTree is a Binary Tree where the value of a node is equal to the
sum of the nodes present in its left subtree and right subtree. An empty tree
is SumTree and the sum of an empty tree can be considered as 0. A leaf node is
also considered as SumTree.

Following is an example of SumTree.
                                      26
                                    /   \
                                  10     3
                                /    \     \
                              4      6      3
"""
#==============================================================================


def is_sum_tree(x: BSTNode) -> bool:
    if not x: return True
    if not x._left and not x._right: return True
    if x._key == _add_subtree(x._left) + _add_subtree(x._right):
        if is_sum_tree(x._left) and is_sum_tree(x._right): return True
    return False


def is_sum_tree_v2(x: BSTNode) -> bool:
    if not x: return True
    if not x._left and not x._right: return True
    sum_subtrees = _add_subtree(x._left) + _add_subtree(x._right)

    if x._key == sum_subtrees:
        return is_sum_tree_v2(x._left) and is_sum_tree_v2(x._right)
    return False


def _add_subtree(x: BSTNode) -> int:
    if not x: return 0
    else: return x._key + _add_subtree(x._left) + _add_subtree(x._right)


def main():
    L = [randrange(10) for _ in range(10)]
    bst = gen_bst(L, type=AVL)
    print(bst, '\n')

    print(bst, '\n')

    assert is_sum_tree_v2(bst)


if __name__ == '__main__':
    main()
