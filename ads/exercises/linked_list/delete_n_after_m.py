from ads.utils.utils import green, red, yellow
from random import randint, randrange
from ads.fundamentals import SLLNode as Node, SLL
#==============================================================================
#==============================================================================
"""
Delete N Nodes After M Nodes in a Singly Linked List.

Example:
    1. delete_n_after_m(SLL([2]).head, 0, 0) -> None
    2. delete_n_after_m(SLL([4, -3]).head, 1, 0) -> SLL([4, -3]).head
    3. delete_n_after_m(SLL([-5, 5, -9]).head, 0, 2) -> None
    4. delete_n_after_m(SLL([-2, -15, -11, -15]).head, 1, 1) -> SLL([-2, -11, -15]).head
    5. delete_n_after_m(SLL([6, -1, -5, -9, -1]).head, 1, 2) -> SLL([6, -9, -1]).head
"""


def delete_n_after_m(head: Node, M: int, N: int) -> Node:
    """Deletes 'N' nodes after 'M' starting from head.

    Args:
        head (Node): The head of the given singly linked list.
        M (int): Number of nodes after which 'N' nodes to be deleted.
        N (int): Number of nodes to be deleted.

    Returns:
        Node: The head of the linked list.
    """
    if not head or M < 0 or N <= 0: return head

    dummy_head = Node(None, head)
    current = dummy_head

    while M > 0 and current:
        current = current._next
        M -= 1

    if not current: return dummy_head._next

    mth = current
    current = current._next
    mth._next = None

    while current and N > 1:
        current = current._next
        N -= 1

    if not current:
        return current
    mth._next = current._next
    current._next = None
    return dummy_head._next


def delete_n_after_m_v2(head: Node, M: int, N: int) -> Node:
    """Deletes 'N' nodes after 'M' starting from head.

    Args:
        head (Node): The head of the given singly linked list.
        M (int): Number of nodes ( M > 0)
        N (int): Number of nodes to be deleted.

    Returns:
        Node: The head of the linked list.
    """
    def size(head):
        sz = 0
        while head:
            sz += 1
            head = head._next
        return sz

    sz = size(head)

    if not head or sz < M or M <= 0 or N <= 0: return head
    # if N > sz - M: return head # another variant of implementaions

    current = head
    while current and M > 1:
        current = current._next
        M -= 1

    Mth = current

    while current and N >= 1:
        current = current._next
        N -= 1

    if not current:
        Mth._next = None
        return head
    else:
        Mth._next = current._next
        current._next = None
        return head


def main():
    functions = [delete_n_after_m, delete_n_after_m_v2]
    L = []

    for f in functions:
        print(f"""{'*'*15} {yellow('Running')}: {f.__name__} {'*'*15}""")
        for i in range(70):
            a = [randint(-15, 15) for _ in range(i)]
            m = randrange(-1, len(a))
            n = randrange(-1, len(a) - m if m >= 0 else 0)

            expected = a if (m < 0 or n < 0) else a[:m] + a[m + n:]
            expected = a if (m == 0 and f == functions[1]) else expected
            expected = None if not a else expected

            sll = SLL(a)
            sll._head = f(sll._head, m, n)
            returned = None if not sll.keys() else sll.keys()
            assert expected == returned

            # returned = f"""SLL({returned}).head""" if returned else None
            # ex = f"""{i}. {f.__name__}(SLL({a}).head, {m}, {n}) -> {returned}"""
            # print(ex)
            # L.append([a, m, n, returned])

    # print(L)


if __name__ == '__main__':
    main()
