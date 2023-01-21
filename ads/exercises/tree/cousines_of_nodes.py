from random import choice, randint, sample

from ads.searching import AVL
from ads.utils import gen_bst, get_subtree, BSTNode as Node
#==============================================================================
""" 993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k 
node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have
different parents.

We are given the root of a binary tree with unique values, and the values x
and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are
cousins.

 

Example 1:
                            1
                          /   \
                        2      3
                      / 
                    4   

Input: root = [1,2,3,4], x = 4, y = 3
Output: false


Example 2:
                            1
                          /  \
                        2     3
                      /  \   / \
                          4     5
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true


Example 3:
                            1
                          /  \
                        2     3
                      /  \
                          4
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:
    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.
"""


# TAKEN FROM: https://www.youtube.com/watch?v=PyfLrJvoC_s
# NOT TESTED THROUGHLY !!
def is_cousines(root: Node, x: int, y: int) -> bool:
    def dfs(root, x, y, depth, parent, x_info, y_info):
        if not root: return None
        if root._key == x: x_info.append((depth, parent))
        if root._key == y: y_info.append((depth, parent))
        dfs(root._left, x, y, depth + 1, root, x_info, y_info)
        dfs(root._right, x, y, depth + 1, root, x_info, y_info)

    x_info = []
    y_info = []
    depth = 0
    # parent = None

    if not root: return None
    dfs(root, x, y, depth, None, x_info, y_info)

    return x_info[0][0] == y_info[0][0] and x_info[0][1] != y_info[0][1]


# TAKEN FROM: https://www.youtube.com/watch?v=UyxnGWMvxwc&t=607s
# NOT TESTED THROUGHLY !!
def is_cousines_v2(root: Node, x: int, y: int) -> bool:
    def height_parent(root: Node, z: int, parent: Node, height: int) -> int:
        if not root: return 0
        if root._key == z: return height

        parent = root
        left_height = height_parent(root._left, z, parent, height + 1)
        right_height = height_parent(root._right, z, parent, height + 1)
        return left_height if left_height else right_height

    if not root: return False
    x_parent = None
    x_height = height_parent(root, x, x_parent, 0)

    y_parent = None
    y_height = height_parent(root, y, y_parent, 0)
    return x_height == y_height and x_parent is not y_parent


def main():
    for _ in range(1):
        L = sample(range(50), 2**4)
        bst = gen_bst(L, type=AVL)
        x_key = choice(L)
        y_key = choice(L)
        n1 = get_subtree(bst, x_key)
        n2 = get_subtree(bst, y_key)
        returned1 = is_cousines_v2(bst, n1, n2)
        returned2 = is_cousines_v2(bst, n1, n2)
        assert returned1 == returned2

        # print(L, x_key, y_key, sep='\t')
        if returned1:
            print(bst)
            print(returned1, x_key, y_key, sep='\t')


if __name__ == '__main__':
    main()
