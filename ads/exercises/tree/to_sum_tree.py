from ads.searching import BSTNode, AVL
from random import randrange

from ads.utils import gen_bst
#==============================================================================
"""
Given a Binary Tree where each node has positive and negative values. Convert
this to a tree where each node contains the sum of the left and right sub trees
in the original tree. The values of leaf nodes are changed to 0.
For example, the following tree .
                  10
               /      \
             -2        6
           /   \      /  \
         8     -4    7    5

should be changed to

                 20(4-2+12+6)
               /      \
         4(8-4)      12(7+5)
           /   \      /  \
         0      0    0    0

"""
#==============================================================================


def convert_to_sumtree(x) -> int:
    if not x: return 0
    left_sumtree = convert_to_sumtree(x._left)
    right_sumtree = convert_to_sumtree(x._right)
    x_old = x._key
    x._key = left_sumtree + right_sumtree
    return x._key + x_old


def to_sum_tree(x: BSTNode) -> int:
    if not x: return 0
    old_val = x.data
    x.data = to_sum_tree(x.left) + to_sum_tree(x.right)
    return x.data + old_val


def main():
    pass


if __name__ == '__main__':
    main()