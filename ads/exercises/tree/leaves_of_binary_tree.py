from ads.searching.bst import AVL
from ads.utils.utils import gen_bst
from random import randint, randrange

from ads.searching import BSTNode as Node
#==============================================================================
""" Counts the number of leaves of a binary tree. """
#==============================================================================


def count_leaves(x: Node):
    if x is None: return 0
    if not x._left and not x._right: return 1
    left_count = count_leaves(x._left)
    right_count = count_leaves(x._right)
    return left_count + right_count


def count_leaves_v2(x: Node) -> int:
    def _count_leaves_v2(x, counter):
        if not x: return None
        if not x._left and not x._right:
            counter[0] += 1
        _count_leaves_v2(x._left, counter)
        _count_leaves_v2(x._right, counter)

    counter = [0]
    _count_leaves_v2(x, counter)
    return counter[0]


#==============================================================================
""" 257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
#==============================================================================


def collect_leaves(x: Node):
    def _collect_leaves(x, res):
        if not x: return
        if not x._left and not x._right: res.append(x._key)
        _collect_leaves(x._left, res)
        _collect_leaves(x._right, res)

    res = []
    _collect_leaves(x, res)
    return res


def leaves_paths(x):
    def _leaves_paths(x, paths, path=[]):
        if not x: return
        path.append(str(x._key))

        if not x._left and not x._right: paths.append("->".join(path))
        _leaves_paths(x._left, paths, path)
        _leaves_paths(x._right, paths, path)
        path.pop()

    paths = []
    _leaves_paths(x, paths)
    return paths


def _test_leaves_paths():
    L = [randrange(1, 1000) for _ in range(20)]
    bst = gen_bst(L)
    print(bst)
    for item in leaves_paths(bst):
        print(item)


def _test_count_leaves():
    for i in range(10):
        L = sorted([randint(-100, 100) for _ in range(2**i)])
        bst = gen_bst(L, type=AVL)
        returned = count_leaves(bst)
        returned_v2 = count_leaves_v2(bst)
        expected = (2**i // 2) if i != 0 else 1
        # print(f"""{'**'*15}""", bst, sep='\n')
        print(returned_v2, returned, expected)
        assert returned == expected == returned_v2


if __name__ == '__main__':
    _test_count_leaves()
    _test_leaves_paths()
