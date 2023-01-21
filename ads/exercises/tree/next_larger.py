#==============================================================================
""" Find the next lerger. - [CtCI: 4.6].

    Write an algorithm to find the'next'node (i.e., in-order successor) of a
    given node in a binary search tree. You may assume that each node has a
    link to its parent """
#==============================================================================


def next_larger(root, key):
    if root is None:
        return
    key_node = _get_key_node(root, key)
    if key_node is None:
        return
    if key_node._right is not None:
        return _min(key_node._right)

    successor = None
    x = root

    while x is not None:
        if key < x._key:
            successor = x
            x = x._left
        elif key > x._key:
            x = x._right
        else:
            return successor


def _get_key_node(x, key):
    if x is None:
        return
    if key < x._key:
        return _get_key_node(x._left, key)
    elif key > x._key:
        return _get_key_node(x._right, key)
    else:
        return x


def _min(x):
    if x is None:
        return
    if x._left is None:
        return x
    else:
        return _min(x._left)


def _test_next_larger():
    L = [randint(0, 999) for _ in range(20)]
    key = choice(L)
    bst = gen_bst(L)
    print(bst._root)
    # print(L)
    print(key)
    res = next_larger(bst._root, key)
    if res is not None:
        print(res._key)
