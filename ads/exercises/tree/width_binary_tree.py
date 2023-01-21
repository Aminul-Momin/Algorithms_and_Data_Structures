""" Compute the width of a binary tree. 

    Examples:
        1. width_bt(gen_bst([])._root) -> -1
        2. width_bt(gen_bst([0])._root) -> 1
        3. width_bt(gen_bst([0, 1])._root) -> 1
        4. width_bt(gen_bst([4, -1, 5])._root) -> 2
        5. width_bt(gen_bst([-5, 1, 4, 1])._root) -> 1
        6. width_bt(gen_bst([0, 1, -4, 1, -3])._root) -> 2
        7. width_bt(gen_bst([2, 0, -1, 4, 2, -3])._root) -> 2
        8. width_bt(gen_bst([3, 2, -1, 0, 5, 1, -3])._root) -> 2
        9. width_bt(gen_bst([1, 0, -2, -1, -3, 2, 3, 0])._root) -> 3
        10. width_bt(gen_bst([1, 0, -1, -2, 5, 3, 0, -1, 1])._root) -> 3
"""

from ads.searching.bst import AVL
from collections import deque
from random import randint

from ads.utils import gen_bst


def width_bt(x):
    if x is None: return -1
    max_width = 0
    q = deque()
    q.append(x)

    while len(q) != 0:
        num_level_nodes = len(q)
        max_width = max(max_width, num_level_nodes)
        while num_level_nodes > 0:
            y = q.popleft()
            if y._left: q.append(y._left)
            if y._right: q.append(y._right)
            num_level_nodes -= 1

    return max_width


def main():
    for i in range(6):
        L = [randint(-20, 20) for _ in range(i * 2)]
        bst = gen_bst(L, type=AVL)
        print(f"""{'*'*20}""", bst, sep='\n')
        returned = width_bt(bst._root)
        print(returned)


if __name__ == '__main__':
    main()