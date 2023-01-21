from random import randint
from ads.fundamentals import SLLNode as Node, SLL
#==============================================================================
"""
Write a program to find the n-th to last element of a Singly Linked List.
[CtCI: 2.2].

Example:
    1. nth_node_from_last(SLL([]).head, 0) -> None
    2. nth_node_from_last(SLL([7]).head, 1) -> Node(7)
    3. nth_node_from_last(SLL([-15, -9]).head, 2) -> Node(-15)
    4. nth_node_from_last(SLL([-14, -7, -12]).head, 0) -> None
    5. nth_node_from_last(SLL([11, 0, -8, 5]).head, 1) -> Node(5)
    6. nth_node_from_last(SLL([-2, -10, 0, 7, 11]).head, 2) -> Node(7)
    7. nth_node_from_last(SLL([-2, -6, 11, 8, 6, 13]).head, 1) -> Node(13)

"""


def nth_node_from_last(x: Node, n: int) -> Node:
    """Find the nth node from last

    Args:
        x (Node): The head of singly linked list
        n (int): Index of the list in 1-based numbering.

    Returns:
        Node: The nth node of this linked list from the last.
    """

    if n == 0 or not x: return None

    current = x
    nth_node = x
    while current is not None and n > 1:
        current = current._next
        n -= 1

    if current is None: return None

    while current._next:
        current = current._next
        nth_node = nth_node._next

    return nth_node


def nth_node_from_last_v2(x: Node, n: int):
    '''It JUST PRINT the n-th node from last, but CAN'T RETURN it.'''

    if n == 0 or not x: return 0
    n_from_last = 1 + nth_node_from_last_v2(x._next, n)
    if n_from_last == n:
        print(f"{n}-th node from the last: {x}")
    return n_from_last


def nth_node_from_last_v3(x: Node, n: int):
    """Find the nth node from last

    Args:
        x (Node): The head of singly linked list
        n (int): Index of the list in 1-based numbering.

    Returns:
        Node: The nth node of this linked list from the last.
    """
    class Index:
        def __init__(self, val):
            self.val = val

    def _nth_from_last(x: Node, n, idx: Index):
        if n <= 0 or not x: return None
        y = _nth_from_last(x._next, n, idx)
        idx.val = idx.val + 1
        if idx.val == n:
            return x
        return y

    return _nth_from_last(x, n, Index(0))


def nth_node_from_last_4(x: Node, n: int):
    """Find the nth node from last

    Args:
        x (Node): The head of singly linked list
        n (int): Index of the list in 1-based numbering.

    Returns:
        Node: The nth node of this linked list from the last.
    """
    current = x
    size = 0
    while current:
        size += 1
        current = current._next

    current = x
    k = size - n

    while k > 0:
        current = current._next
        k -= 1

    return current


def main():
    functions = [
        nth_node_from_last, nth_node_from_last_v3, nth_node_from_last_4
    ]

    for f in functions:
        for i in range(7):
            given_a = [randint(-15, 15) for _ in range(i)]
            given_idx = randint(0, len(given_a))
            expected = given_a[-given_idx] if given_idx else None

            sll = SLL(given_a)
            res = f(sll._head, given_idx)
            returned = res._key if res and given_idx else None

            assert returned == expected

            # returned = f"""Node({returned})""" if returned else None
            # exmample = f"""{i+1}. {f.__name__}(SLL({given_a}).head, {given_idx}) -> {returned}"""
            # print(exmample)

        print(f"""{'*'*15} Running: {f.__name__} {'*'*15}""")


if __name__ == '__main__':
    main()
