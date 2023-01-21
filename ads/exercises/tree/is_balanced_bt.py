from ads.searching.bst import AVL
from random import randint
from ads.utils import gen_bst, gen_bt
#==============================================================================
""" Implement a function to check if a binary tree is height balanced. - [EPI: 9.1]. """
#==============================================================================


def is_balanced_BT_1(x):
    return _is_balanced_BT_1(x) != -1


def _is_balanced_BT_1(x):
    if x is None:
        return 0

    left_res = _is_balanced_BT_1(x._left)
    if left_res == -1:
        return -1

    right_res = _is_balanced_BT_1(x._right)
    if right_res == -1:
        return -1

    height_diff = left_res - right_res

    if abs(height_diff) > 1:
        return -1
    return max(left_res, right_res) + 1


def is_balanced_BT_2(x):
    return _is_balanced_BT_2(x)[1]


def _is_balanced_BT_2(x):
    if x is None:
        return (0, True)

    left_res = _is_balanced_BT_2(x._left)
    if not left_res[1]:
        return left_res

    right_res = _is_balanced_BT_2(x._right)
    if not right_res[1]:
        return right_res

    is_balanced = abs(left_res[0] - right_res[0]) <= 1

    return (max(left_res[0], right_res[0]) + 1, is_balanced)


def main():
    for _ in range(10):
        L1 = sorted([randint(-20, 20) for i in range(10)], reverse=True)

        bst1 = gen_bst(L1, type=AVL)  # generates a balanced BST
        assert is_balanced_BT_1(bst1)

        bst2 = gen_bst(L1)  # generate unbalanced BST
        assert not is_balanced_BT_2(bst2)

        bst3 = gen_bt(L1)  # generate balanced BST
        assert is_balanced_BT_2(bst3)


if __name__ == '__main__':
    main()
