from collections import deque
from ads.searching import BSTNode as Node

#==============================================================================
""" Binary Tree Spiral-Order Traversal

Given the root of a binary tree, return the spiral-order traversal of its
nodes' values.
"""
#==============================================================================


def spiral_order(x: Node) -> None:
    spiral = []
    stk1 = deque()
    stk2 = deque()
    stk1.append(x)

    while stk1 or stk2:

        while stk1:
            current = stk1.pop()
            spiral.append(current._key)
            if current._left: stk2.append(current._left)
            if current._right: stk2.append(current._right)

        while stk2:
            current = stk2.pop()
            spiral.append(current._key)
            if current._right: stk1.append(current._right)
            if current._left: stk1.append(current._left)

    return spiral

def main():
    pass


if __name__ == '__main__':
    main()
