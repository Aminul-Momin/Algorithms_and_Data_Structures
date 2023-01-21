#==============================================================================
""" Create Linked Lists of all the nodes at each depth of a BT. """
#==============================================================================


def linkedlist_from_BT(x):
    lists = []
    _linkedlist_from_BT(x, lists)
    return lists


def _linkedlist_from_BT(x, lists):
    q = []
    if x is not None:
        q.append(x)
    while len(q) != 0:
        current = deque()
        level_size = len(q)

        while level_size > 0:
            temp = q.pop(0)
            current.append(temp._key)

            if temp._left is not None:
                q.append(temp._left)
            if temp._right is not None:
                q.append(temp._right)

            level_size -= 1

        lists.append(tuple(current))
        current.clear()


def _test_linkedlist_from_BT():
    bst = gen_bst()
    print(bst)
    list_of_Linkedlist = linkedlist_from_BT(bst._root)

    for linkedlist in list_of_Linkedlist:
        print(linkedlist)
