from random import randint

from ads.searching import BSTNode
from ads.utils import gen_bst
#==============================================================================
""" Compute the height of a binary tree.

    Examples:
        NOTE: `gen_bst(list)` is a function which generates a binary search
            tree out of the given list and returns the root of that tree.

        1. height_bt(gen_bst([])) -> -1
        2. height_bt(gen_bst([-3])) -> 0
        3. height_bt(gen_bst([-3, 4])) -> 1
        4. height_bt(gen_bst([2, 5, -4])) -> 1
        5. height_bt(gen_bst([1, -5, -1, -4])) -> 3
        6. height_bt(gen_bst([0, -1, -1, 1, -1])) -> 3
        7. height_bt(gen_bst([1, 1, 3, 3, -3, 2])) -> 3
        8. height_bt(gen_bst([-3, 3, 4, -4, 0, -2, 5])) -> 3
        9. height_bt(gen_bst([1, -5, -1, -5, -3, -4, 4, 5])) -> 5
"""


def height_bt_v1(x: BSTNode) -> int:
    """Computes the height of a binary tree in terms of zero-based numbering.

    Returns:
        The height of the given tree.
    """
    if not x: return -1
    left = height_bt_v1(x._left)
    right = height_bt_v1(x._right)
    return max(left, right) + 1


def height_bt_v2(x: BSTNode) -> int:
    """Computes the height of a binary tree in terms of zero-based numbering.

    Returns:
        The height of the given tree.
    """
    if not x: return 0
    left = height_bt_v2(x._left)
    right = height_bt_v2(x._right)
    return max(left, right) + 1


def main():
    bst = gen_bst([randint(0, 20) for _ in range(7)])
    returned1 = height_bt_v1(bst)
    returned2 = height_bt_v2(bst)
    assert returned2 == 1 + returned1
    print(bst, returned1, sep='\n\n')


if __name__ == '__main__':
    main()
