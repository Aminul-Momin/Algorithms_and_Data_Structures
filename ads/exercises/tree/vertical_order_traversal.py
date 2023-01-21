from ads.searching import BSTNode as Node
#==============================================================================
""" Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the
binary tree.

For each node at position (row, col), its left and right children will be at
positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of
the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom
orderings for each column index starting from the leftmost column and ending
on the rightmost column. There may be multiple nodes in the same row and same
column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

Constraints:
    1) The number of nodes in the tree is in the range [1, 1000].
    2) 0 <= Node.val <= 1000
"""
#==============================================================================


def vertical_order(x: Node) -> None:
    def _vertical_order(x, hd, hd_elms):
        if not x: return None
        _vertical_order(x._left, hd - 1, hd_elms)

        hd_elms[hd] = hd_elms.get(hd, []) + [x._key]
        _vertical_order(x._right, hd + 1, hd_elms)

    hd_elms = {}
    hd = 0
    _vertical_order(x, hd, hd_elms)
    result = [val for val in hd_elms.values()]
    return result

def main():
    pass


if __name__ == '__main__':
    main()
