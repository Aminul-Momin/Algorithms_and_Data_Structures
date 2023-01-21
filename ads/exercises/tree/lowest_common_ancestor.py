from random import randrange, choice
from ads.utils import gen_bst, get_subtree
#==============================================================================
""" Find the lowest common ancestor of a binary tree. - [EPI: 9.3, EPI: 12.4, EPI: 14.4]

    Design an algorithm and write code to find the first common ancestor of
    two nodes in a binary tree. Avoid storing additional nodes in a data
    structure.

    NOTE: This is not necessarily a binary search tree. """
#==============================================================================


def lowest_common_ancestor(x, n1, n2):
    if not x: return None
    if x._key == n1._key or x._key == n2._key: return x

    left_result = lowest_common_ancestor(x._left, n1, n2)
    right_result = lowest_common_ancestor(x._right, n1, n2)

    if left_result and right_result: return x
    if left_result: return left_result
    if right_result: return right_result

    return None


# compute the LCA of BST of distinct keys from top.
# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA(x, s, b):
    '''
    x: the root of a binary search tree.
    s: smaller one of two nodes whose LCA is to find.
    b: bigger one of two nodes whose LCA is to find.
    '''

    # Keep searching since tree is outside of [s, b].
    while x._key < s._key or x._key > b._key:
        while x._key < s._key:
            x = x._right  # LCA must be in x's right subtree
        while x._key > b._key:
            x = x._left  # LCA must be in x's left subtree

        # Now, s.data <= tree.data && tree.data <= b.data.
        return x


def lca_close_ancestor_with_parent_pntr(x, y):

    n1, n2 = x, y
    nodes_on_path_to_root = set()

    while n1 or n2:
        # Ascend tree in tandem for these two nodes.
        if n1:
            if n1 in nodes_on_path_to_root: return n1
            nodes_on_path_to_root.add(n1)
            n1 = n1.parent
        if n2:
            if n2 in nodes_on_path_to_root: return n2
            nodes_on_path_to_root.add(n2)
            n2 = n2.parent

    raise ValueError('x and y are not in the same tree')


def lca_with_parent_pntr(x, y):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth_x, depth_y = map(get_depth, (x, y))

    # Makes x as the deeper node in order to simplify the code.
    if depth_y > depth_x: x, y = y, x

    # Ascends from the deeper node.
    depth_diff = abs(depth_x - depth_y)
    while depth_diff:
        x = x.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while x is not y:
        x, y = x.parent, y.parent

    return x


def _test_lowest_common_ancestor():

    L = [randrange(10, 100) for _ in range(15)]
    bst = gen_bst(L)
    n1 = get_subtree(bst._root, choice(L))
    n2 = get_subtree(bst._root, choice(L))
    lcw = lowest_common_ancestor(bst._root, n1, n2)

    lcw2 = find_LCA(bst._root, n1, n2)

    print(bst, '\n', '*' * 20)
    print('key of Node1: ', n1._key, '\nkey of Node2: ', n2._key)
    print('Their lowest common ancestor: ', lcw._key)


def main():
    pass


if __name__ == '__main__':
    main()
