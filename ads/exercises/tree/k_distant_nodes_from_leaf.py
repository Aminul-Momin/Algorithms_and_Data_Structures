#==============================================================================
"""  Print the nodes of K distance from LEAF. """
# NOT WORKING !!
#==============================================================================


def nodes_distant_k_from_leaf(x, k):
    '''Print the nodes at kth distant of one-based indexing'''
    if not x: return 0

    left_res = nodes_distant_k_from_leaf(x._left, k - 1)
    if left_res == k: print(x._key)

    right_res = nodes_distant_k_from_leaf(x._right, k - 1)
    if right_res == k: print(x._key)


def _test_nodes_distant_k_from_leaf():
    L = [randint(0, 999) for _ in range(10)]
    bst = gen_bst(L)
    print(bst._root)
    nodes_distant_k_from_leaf(bst._root, 3)