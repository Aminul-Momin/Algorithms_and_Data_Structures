from random import randint
from typing import Iterable

from ads.utils import gen_bst
from ads.searching import BSTNode as Node, BST, AVL
#==============================================================================
""" Count the number of full nodes of a binary tree.

Examples:
                          ...10..
                         /       \
                       .5..       13
                      /    \     /  \
                      3     7   11  14
                     / \   / \  /\   /\
                    2  4  6  8        15
                    /\ /\ /\ /\        /\
                                        16
                                       /\
Number of full nodes: 5
Full nodes are: [3, 5, 7, 10, 13]
"""
#==============================================================================


def count_full_nodes(x: Node) -> int:
    if not x: return 0

    left_res = count_full_nodes(x._left)
    right_res = count_full_nodes(x._right)

    if left_res and right_res: return left_res + right_res + 1
    if left_res and x._left and x._right: return left_res + 1
    if right_res and x._left and x._right: return right_res + 1

    if x._left and x._right: return 1

    return left_res + right_res


def count_full_nodes_v2(x: Node) -> int:
    def _count(x, counter):
        if not x: return None
        if x._left and x._right: counter[0] += 1
        _count(x._left, counter)
        _count(x._right, counter)

    counter = [0]
    _count(x, counter)
    return counter[0]

# NOT WORKING
def count_full_nodes_v3(x: Node) -> int:
    if not x: return 0
    if not x._left and not x._right: return 1
    return count_full_nodes_v3(x._left) + count_full_nodes_v3(x._right) + 1

#==============================================================================
""" Collect the ull nodes of a binary tree. """
#==============================================================================


def collect_full_nodes_v1(x) -> Iterable:
    def _collect_full_nodes_v1(x, nodes):
        if not x: return None
        if x._left and x._right: nodes.append(x._key)
        _collect_full_nodes_v1(x._left, nodes)
        _collect_full_nodes_v1(x._right, nodes)

    nodes = []
    _collect_full_nodes_v1(x, nodes)
    return nodes


def collect_full_nodes_v2(x: Node):
    def _collect_full_nodes_v2(x, res):
        if x is None: return None
        _collect_full_nodes_v2(x._left, res)
        _collect_full_nodes_v2(x._right, res)
        if x._left and x._right: res.append(x._key)

    res = []
    _collect_full_nodes_v2(x, res)
    return res


def main():
    for _ in range(10):
        bst = gen_bst([randint(-20, 20) for _ in range(15)], type=AVL)
        nodes_count1 = count_full_nodes(bst)
        nodes_count2 = count_full_nodes_v2(bst)
        nodes_count3 = count_full_nodes_v3(bst)
        full_nds1 = collect_full_nodes_v1(bst)
        full_nds2 = collect_full_nodes_v2(bst)

        # assert nodes_count1 == nodes_count2 == nodes_count3
        # assert full_nds1.sort() == full_nds2.sort()

        print(bst,
              f"Number of full Nodes: {nodes_count1}",
              f"Number of full Nodes: {nodes_count2}",
              f"Number of full Nodes: {nodes_count3}",
            #   f"Full Nodes: {full_nds1}",
              sep='\n')


if __name__ == '__main__':
    main()
