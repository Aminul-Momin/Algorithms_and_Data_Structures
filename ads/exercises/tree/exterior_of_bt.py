from random import randint

from ads.searching import BSTNode as Node
from ads.utils import gen_bst
#==============================================================================
"""
The exterior of a binary tree is the following sequences of nodes: the nodes
from the root to the leftmost leaf, followed by the leaves in left-to-right
order, followed by the nodes from the rightmost leaf to the root. By leftmost
(rightmost) leaf, we mean the leaf that appears first (last) in an inorder
traversal

Write a program that computes the exterior of a binary tree.
"""


def exterior_binary_tree(tree):

    # Computes the nodes from the root to the leftmost leaf.
    def left_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right): return
        exterior.append(subtree)
        if subtree.left: left_boundary(subtree.left)
        else: left_boundary(subtree.right)

    # Computes the nodes from the rightmost leaf to the root.
    def right_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right): return
        if subtree.right: right_boundary(subtree.right)
        else: right_boundary(subtree.left)
        exterior.append(subtree)

    # Compute the leaves in left-to-right order.
    def leaves(subtree):
        if not subtree: return
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return
        leaves(subtree.left)
        leaves(subtree.right)

    if not tree: return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior


def create_output_list(L):
    if any(l is None for l in L):
        raise Exception('Resulting list contains None')
    return [l.data for l in L]


def main():
    pass


if __name__ == '__main__':
    main()