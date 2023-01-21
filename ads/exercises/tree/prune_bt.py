from random import randint

from ads.searching import BSTNode as Node
from ads.utils import gen_bst
#==============================================================================
""" 814. Binary Tree Pruning

Given the root of a binary tree, return the same tree where every subtree
(of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

 

Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
 

Constraints:
    1) The number of nodes in the tree is in the range [1, 200].
    2) Node.val is either 0 or 1.
"""


def prune_tree(root: Node) -> Node:
    def contain_one(root) -> bool:
        if not root: return False
        left_contains = contain_one(root._left)
        right_contains = contain_one(root._right)
        if not left_contains: root._left = None
        if not right_contains: root._right = None
        return root._key == 1 or left_contains or right_contains

    if not root: return None
    contain_one(root)
    return root


def main():
    pass


if __name__ == '__main__':
    main()
