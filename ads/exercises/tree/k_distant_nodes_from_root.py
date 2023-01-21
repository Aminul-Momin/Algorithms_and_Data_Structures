#==============================================================================
"""  Print the nodes of K distance from ROOT. """
#==============================================================================


def nodes_distant_k(x, k):
    '''Print the nodes at kth distant of one-based indexing'''
    if not x: return
    if k == 1: print(x._key)
    nodes_distant_k(x._left, k - 1)
    nodes_distant_k(x._right, k - 1)


def _test_nodes_distant_k():
    L = [randint(0, 999) for _ in range(10)]
    avl = gen_bst(L, type=AVL)
    print(avl)
    nodes_distant_k(avl, 6)