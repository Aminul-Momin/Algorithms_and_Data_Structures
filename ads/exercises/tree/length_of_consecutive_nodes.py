from random import randint

from ads.utils import BSTNode as Node, gen_bst
#==============================================================================
""" 298. Binary Tree Longest Consecutive Sequence

Given a binary tree, write function to find the length of longest branches of
nodes in increasing consecutive order.
                            0
                          /   \
                        1      2
                      /  \   /  \
                    1     2 1    3
            
            Length : 3
"""


def find_consecutive_length(x: Node) -> int:
    def consecutive_length(x: Node, parent_key: int, length) -> int:
        if not x: return length
        if x._key == parent_key + 1:
            left_child_len = consecutive_length(x._left, x._key, length + 1)
            right_child_len = consecutive_length(x._right, x._key, length + 1)
            return max(left_child_len, right_child_len)
        else:
            left_child_len = consecutive_length(x._left, x._key, 1)
            right_child_len = consecutive_length(x._right, x._key, 1)
            return max(length, left_child_len, right_child_len)

    if not x: return 0
    left_child_len = consecutive_length(x._left, x._key, 1)
    right_child_len = consecutive_length(x._right, x._key, 1)
    return max(left_child_len, right_child_len)


def find_consecutive_length_v2(root: Node) -> int:
    def consecutive_length(root, count, target, res):
        if not root: return None
        elif root._key == target: count += 1
        else: count = 1
        res[0] = max(res[0], count)
        consecutive_length(root._left, count, root._key + 1, res)
        consecutive_length(root._right, count, root._key + 1, res)

    res = [0]
    consecutive_length(root, 0, 0, res)
    return res[0]


def main():
    for _ in range(5):
        L = [randint(-5, 5) for _ in range(10)]
        bst = gen_bst(L)
        print(bst)
        returned1 = find_consecutive_length(bst)
        returned2 = find_consecutive_length_v2(bst)
        assert returned1 == returned2
        print(returned1)


if __name__ == '__main__':
    main()
