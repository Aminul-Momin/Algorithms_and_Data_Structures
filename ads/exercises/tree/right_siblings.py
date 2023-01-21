#==============================================================================
"""
For this problem, assume that each binary tree node has a extra field, call
it level-next, that holds a binary tree node (this field is distince from the
fields for the left and right children). The level-next field will be used to
compute a map from nodes to their right siblings. The input is assumed to be
perfect binary tree.

Write a program that takes a perfect binary tree, and sets each node's level-
next field to thenode on its right, if one exists. [EPI: 9.16]
"""


class Node:
    def __init__(self, key=None):
        self._data = key
        self._left = None
        self._right = None
        self._next = None  # Populates this field.


def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node._left:
            # Populate left child's next field.
            start_node._left._next = start_node._right
            # Populate right child's next field if start_node is not the last
            # node of level.
            start_node._right._next = start_node._next and start_node._next._left
            start_node = start_node._next

    while tree and tree._left:
        populate_children_next_field(tree)
        tree = tree._left


def traverse_next(node):
    while node:
        yield node
        node = node._next
    raise StopIteration


def traverse_left(node):
    while node:
        yield node
        node = node._left
    raise StopIteration


def clone_tree(original):
    if not original: return None
    cloned = Node(original._key)
    cloned._left = clone_tree(original._left)
    cloned._right = clone_tree(original._right)
    return cloned
