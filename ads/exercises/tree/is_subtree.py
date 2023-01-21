#==============================================================================
""" Check if one tree is a subtree of another tree. """
#==============================================================================


def is_subtree(x, s):
    if not s: return True
    if not x: return False
    if is_identical(x, s): return True
    left_res = is_subtree(x._left, s)
    right_res = is_subtree(x._right, s)
    return left_res or right_res


def is_identical(s1, s2):
    if s1 is None and s2 is None: return True
    if s1 is None or s2 is None: return False

    if s1._key == s2._key:
        left_res = is_identical(s1._left, s2._left)
        right_res = is_identical(s1._right, s2._right)
        return left_res and right_res
    else:
        return False


def _test_is_subtree():

    M = [randint(0, 999) for _ in range(20)]
    key = choice(M)
    main_tree = gen_bst(M, type='avl')
    sub_tree = get_subtree(main_tree._root, key)
    print(main_tree, '\n' * 2, sub_tree)
    print(is_subtree(main_tree._root, sub_tree))
