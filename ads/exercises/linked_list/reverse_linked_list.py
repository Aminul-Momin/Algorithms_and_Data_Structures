from random import randint
from ads.fundamentals import SLLNode as Node, SLL
#==============================================================================
""" Reverse a Linked list.

Example:
    1. reverse_sll_v2(SLL([]).head) -> SLL([]).head)
    2. reverse_sll_v2(SLL([8]).head) -> SLL([8]).head)
    3. reverse_sll_v2(SLL([-7, -10]).head) -> SLL([-10, -7]).head)
    4. reverse_sll_v2(SLL([-2, 8, 12]).head) -> SLL([12, 8, -2]).head)
    5. reverse_sll_v2(SLL([5, 6, -8, 13]).head) -> SLL([13, -8, 6, 5]).head)
    6. reverse_sll_v2(SLL([-5, 3, 7, -3, 7]).head) -> SLL([7, -3, 7, 3, -5]).head)
"""


def reverse_sll(x: Node) -> Node:
    """Reverse the given singly linked list recursively

    Args:
        x (Node): the head of the linked list.

    Returns:
        Node: the head of the reversed linked list.
    """
    if x is None or x._next is None: return x
    new_head = reverse_sll(x._next)
    x._next._next = x
    x._next = None
    return new_head


def reverse_sll_v2(x: Node) -> Node:
    """Reverse the given singly linked list recursively

    Args:
        x (Node): the head of the linked list.

    Returns:
        Node: the head of the reversed linked list.
    """
    if x is None or x._next is None: return x
    second = x._next
    x._next = None
    rest = reverse_sll_v2(second)
    second._next = x
    return rest


def reverse_sll_itr(x: Node) -> Node:
    """Reverse the given singly linked list recursively

    Args:
        x (Node): the head of the linked list.

    Returns:
        Node: the head of the reversed linked list.
    """
    if not x: return x
    current = x
    prev = None
    while True:
        second = current._next
        current._next = prev
        prev = current

        if not second: break
        current = second

    return current


def reverse_sll_itr_v2(x: Node) -> Node:
    """Reverse the given singly linked list recursively

    Args:
        x (Node): the head of the linked list.

    Returns:
        Node: the head of the reversed linked list.
    """
    if not x: return x
    current = x
    prev = None
    while current:
        second = current._next
        current._next = prev
        prev = current
        current = second

        if not second: return prev


def main():
    functions = [
        reverse_sll, reverse_sll_v2, reverse_sll_itr, reverse_sll_itr_v2
    ]

    for f in functions:
        print(f"""{'*'*15} Running: {f.__name__} {'*'*15}""")
        for i in range(70):
            a = [randint(-15, 15) for _ in range(i)]
            a_reversed = [*reversed(a)]
            sll = SLL(a)
            sll._head = f(sll._head)
            rev = sll.keys()

            assert a_reversed == rev

        #     exmample = f"""{i+1}. {f.__name__}(SLL({a}).head) -> SLL({rev}).head)"""
        #     print(exmample)


if __name__ == '__main__':
    main()
