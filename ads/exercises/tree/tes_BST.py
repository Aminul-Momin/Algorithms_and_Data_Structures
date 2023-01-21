from random import randrange, randint
import unittest

import BST as bst


@pytest.mark.skip(reason='not now')
class TestBST(unittest.TestCase):
    def setUp(self):
        # Creates a sum tree.
        sum_tree = generate_sum_tree()

        # Creates a Tree whose subtree is sumTree.
        main_tree = Node(10)
        main_tree.left = generate_sum_tree()

        # creates a mirror tree of bst1.
        mirror_tree = generate_mirror_tree()


    def tearDown(self):
        pass

    def test_lowest_common_ancestor(self):
         pass


class Node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key              # the key
        self.left = left            # left subtree
        self.right = right          # right subtree


def generate_sum_tree():
    sumTree = Node(40)
    sumTree.left = Node(6)
    sumTree.right = Node(14)
    sumTree.left.left = Node(2)
    sumTree.right.right = Node(8)
    sumTree.left.right = Node(4)
    sumTree.right.left = Node(6)
    return sumTree


def generate_mirror_tree():
    mirrorTree = Node(5)
    mirrorTree.left = Node(7)
    mirrorTree.right = Node(3)
    mirrorTree.left.left = Node(8)
    mirrorTree.right.right = Node(2)
    mirrorTree.left.right = Node(6)
    mirrorTree.right.left = Node(4)
    return mirrorTree

