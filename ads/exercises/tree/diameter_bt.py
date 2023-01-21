from ads.exercises.tree.height_bt import height_bt_v1, height_bt_v2
from ads.utils import gen_bst
#==============================================================================
""" Compute the Diameter of the given Binary Search Tree. """
#==============================================================================


def diameter_BST1(x):
    if x is None: return 0
    left_height = height_bt_v1(x._left)
    right_height = height_bt_v1(x._right)

    left_diameter = diameter_BST1(x._left)
    right_diameter = diameter_BST1(x._right)

    return max(left_height + right_height + 3,
               max(left_diameter, right_diameter))


def diameter_BST2(x):
    if x is None: return 0
    left_diameter = diameter_BST2(x._left)
    right_diameter = diameter_BST2(x._right)
    left_height = height_bt_v2(x._left)
    right_height = height_bt_v2(x._right)
    return max(left_height + right_height + 1,
               max(left_diameter, right_diameter))


def _test_diameter_BST():
    bst = gen_bst()
    print(bst)

    diameter1 = diameter_BST1(bst._root)
    diameter2 = diameter_BST2(bst._root)
    assert diameter1 == diameter2
    print('diameter of BST by diameter_BST1: ', diameter1)
    print('diameter of BST by diameter_BST2: ', diameter2)
