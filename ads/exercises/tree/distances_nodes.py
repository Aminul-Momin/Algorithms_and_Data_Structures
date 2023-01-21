from random import randrange, choice
from ads.utils import gen_bst, get_subtree

from ads.exercises.tree.lowest_common_ancestor import lowest_common_ancestor
#==============================================================================
""" Find the distance of two nodes of a Binary Tree. """
#==============================================================================


def get_distance(x, s1, s2):
    lca = lowest_common_ancestor(x, s1, s2)
    dist_lca_s1 = path_length(lca, s1)
    dist_lca_s2 = path_length(lca, s2)
    return dist_lca_s1 + dist_lca_s2


def path_length(x, s1):
    if not x or s1 is None: return -1
    if x._key == s1._key: return 0

    left_res = path_length(x._left, s1)
    if left_res != -1: return 1 + left_res

    right_res = path_length(x._right, s1)
    if right_res != -1: return 1 + right_res

    return -1


def main():
    L = [randrange(10, 100) for _ in range(20)]
    bst = gen_bst(L)
    n1 = get_subtree(bst._root, choice(L))
    n2 = get_subtree(bst._root, choice(L))
    lca = lowest_common_ancestor(bst._root, n1, n2)
    print(lca, '\n' * 2, n1, n2)
    print(get_distance(bst._root, n1, n2))


if __name__ == '__main__':
    main()
