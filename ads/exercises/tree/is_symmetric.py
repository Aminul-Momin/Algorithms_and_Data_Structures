from random import randrange

from ads.exercises.tree.invert_bt import invert_bt
from ads.utils import gen_bst
from ads.searching._nodes import BSTNode
#==============================================================================
""" Check if one tree is a mirror of another tree. Alternatively, Test if binary is symmetric. - [EPI: 9.2]. """
#==============================================================================


def is_symmetric(root):
    def check_symmetry(x: BSTNode, y: BSTNode) -> bool:
        """Find whether the given trees `x` and `y` are symmetric or not.
        
        Args:
            x: the one binary tree.
            y: the other binary tree.
        """
        if not x and not y: return True
        if not x or not y: return False
        if x._key == y._key:
            left_right = check_symmetry(x._left, y._right)
            right_left = check_symmetry(x._right, y._left)
            return left_right and right_left
        return False

    return not root or check_symmetry(root._left, root._right)


def is_mirror(tree: BSTNode) -> bool:
    """Find whether the given `tree` is symmetric or not.

    Args:
        tree (BSTNode): The tree whose symmetry is to be tested

    Returns:
        bool: True if the given `tree` is symmetric, False otherwise.
    """
    def _mirror(x: BSTNode, y: BSTNode) -> bool:
        """Find whether the given trees `x` and `y` are mirror to each other or not.
        Args:
            x: the left subtree.
            y: the right subtree.
        """
        if not x and not y: return True
        if x and y and x._key == y._key:
            return _mirror(x._left, y._right) and _mirror(x._right, y._left)
        return False  # One subtree is empty, but the other is not.

    return not tree or _mirror(tree._left, tree._right)


def main():
    L = [randrange(10, 100) for _ in range(15)]
    bst1 = gen_bst(L)
    bst2 = invert_bt(gen_bst(L))
    print(bst1, bst2, sep='\n')

    assert is_symmetric(bst1, bst2)


if __name__ == '__main__':
    main()
