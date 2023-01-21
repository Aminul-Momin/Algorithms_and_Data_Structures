from collections import deque
from random import randint

from ads.searching import BSTNode as Node
from ads.utils import gen_bst
#==============================================================================
"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:
                            1     <-
                          /  \
                        2     3   <-
                         \     \
                          5     4 <-



Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:
    1) The number of nodes in the tree is in the range [0, 100].
    2) -100 <= Node.val <= 100
"""


def right_view_bt(root: Node):
    viewed_from_right = []
    q = deque()
    q.append(root)

    while q:
        size = len(q)
        for i in range(size):
            current = q.popleft()
            if i == size - 1: viewed_from_right.append(current._key)
            if current._left: q.append(current._left)
            if current._right: q.append(current._right)

    return viewed_from_right


def main():
    L = [randint(-20, 20) for _ in range(20)]
    bst = gen_bst(L)
    returned = right_view_bt(bst)
    print(bst, returned, sep='\n\n')


if __name__ == '__main__':
    main()
