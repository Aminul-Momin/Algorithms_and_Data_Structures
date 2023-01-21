#==============================================================================
""" Print the nodes of having K leaves in its subtree. """
#==============================================================================


def nodes_of_k_leaves(x, k):
    if not x: return 0
    if not x._left and not x._right: return 1

    left_leaves = nodes_of_k_leaves(x._left, k)
    right_leaves = nodes_of_k_leaves(x._right, k)

    total_leaves = left_leaves + right_leaves

    if total_leaves == k: print(x._key)

    return total_leaves


def _test_nodes_of_k_leaves():
    L = [randint(1, 999) for _ in range(20)]
    bst = gen_bst(L)
    print(bst._root)
    nodes_of_k_leaves(bst._root, 4)
