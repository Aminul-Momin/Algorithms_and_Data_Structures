from random import randrange
from ads.utils import gen_bst, gen_bt
#==============================================================================
"""
Given a binary tree, check whether it is a binary search tree or not
- Example:
    1. is_BST(gen_bt([-5, -5, -5, -2, 0, 2, 4, 9])) -> True
    2. is_BST(gen_bt([-5, -2, -5, 4, 0, 2, 9, -5])) -> False
    3. is_BST(gen_bt([-5, -4, -4, 0, 0, 4, 8, 9])) -> True
    4. is_BST(gen_bt([0, 9, -4, 0, -4, -5, 4, 8])) -> False
    5. is_BST(gen_bt([-10, -9, -8, -6, -6, 3, 3, 6])) -> True
    6. is_BST(gen_bt([-8, 3, 6, 3, -6, -9, -6, -10])) -> False
    7. is_BST(gen_bt([-9, -9, -7, -3, 1, 7, 7, 9])) -> True
    8. is_BST(gen_bt([-9, -3, 1, -7, 9, 7, 7, -9])) -> False
    9. is_BST(gen_bt([-9, -9, -7, -6, -3, -3, -3, 9])) -> True
"""
#==============================================================================

def is_BST(x):
    def _is_BST(x, smaller, larger):
        if x is None: return True
        if smaller and x._key < smaller._key: return False
        if larger and x._key > larger._key: return False
        return _is_BST(x._left, smaller, x) and _is_BST(x._right, x, larger)

    return _is_BST(x, None, None)


def main():
    for i in range(5):
        L = [randrange(-10, 10) for _ in range(8)]
        bst, bt = gen_bt(sorted(L)), gen_bt(L)
        res1 = is_BST(bst)
        res2 = is_BST(bt)

        assert res1 and not res2

        if not res1: print(bst)
        if res2: print(bt)

if __name__ == '__main__':
    main()
