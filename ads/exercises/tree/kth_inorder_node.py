from random import randint

from ads.utils import gen_bst
#==============================================================================
"""
Write a function that efficiently computes the kth node appearing in an
inorder traversal. Assume that each node stores the number of nodes in the
subtree rooted at that node. [EPI: 9.9]
"""
#==============================================================================


class Node:
    def __init__(self, key=None, left=None, right=None, size=None):
        self._key = key
        self._left = left
        self._right = right
        self._size = size


def find_kth_node_bt(tree, k):

    while tree:
        left_size = tree._left._size if tree._left else 0
        if left_size + 1 < k:  # k-th node must be in right subtree of tree.
            k -= left_size + 1
            tree = tree._right
        elif left_size == k - 1:  # k-th is iter itself.
            return tree
        else:  # k-th node must be in left subtree of iter.
            tree = tree._left
    return None  # If k is between 1 and the tree size, this is unreachable.


def main():
    bst = gen_bst([randint(0, 20) for _ in range(15)])
    k = randint(0, 15)
    print(bst, f"K: {k}", find_kth_node_bt(bst, k), sep='\n\n')


if __name__ == '__main__':
    main()
