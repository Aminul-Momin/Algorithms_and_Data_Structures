from random import randrange
from ads.utils import gen_bst
#==============================================================================
"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:
                4                                  4
              /  \                               /  \
            2     7           =====>>          7     2
          /  \   / \                         /  \   / \
        1     3 6   9                      9     6 3   1


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:
    1) The number of nodes in the tree is in the range [0, 100].
    2) -100 <= Node.val <= 100
"""


def invert_bt(x):
    if not x: return None
    left_child = invert_bt(x._left)
    right_child = invert_bt(x._right)
    x._left = right_child
    x._right = left_child
    return x


def invert_bt_v2(tree):
    if not tree: return None
    tree._left, tree._right = tree._right, tree._left
    invert_bt_v2(tree._left)
    invert_bt_v2(tree._right)


def main():
    functions = [invert_bt, invert_bt_v2]
    for f in functions:
        print(f"""{'*'*20} Running: {f.__name__} {'*'*20}""")
        L = [randrange(1, 1000) for _ in range(20)]
        bst = gen_bst(L)
        print("Before Invertion:", bst, sep='\n')
        f(bst)
        print("After Invertion:", bst, sep='\n')


if __name__ == '__main__':
    main()
