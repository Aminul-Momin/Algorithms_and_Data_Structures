from random import randint

from ads.utils import gen_bst
from ads.searching import BSTNode as Node
#==============================================================================
"""
Find the Max element in a Given Binary Tree.
Note: The specified tree may not be a Binary Search Tree.
"""


def max_binary_tree(x: Node):
    if x is None: return float('-inf')
    return max(x._key, max_binary_tree(x._left), max_binary_tree(x._right))


def main():
    bst = gen_bst([randint(0, 20) for _ in range(7)])
    print(bst, max_binary_tree(bst), sep='\n\n')


if __name__ == '__main__':
    main()
