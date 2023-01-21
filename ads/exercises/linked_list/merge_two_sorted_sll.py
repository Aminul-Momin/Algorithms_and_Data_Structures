from random import randint
from ads.fundamentals import SLLNode as Node, SLL
#==============================================================================
""" Merge or Combine Two Sorted Linked Lists.

Merge two sorted linked lists and return it as a sorted list. The list should
be made by splicing together the nodes of the first two lists.

 

Example 1:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: l1 = [], l2 = []
    Output: []

Example 3:
    Input: l1 = [], l2 = [0]
    Output: [0]
 
Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.


Examples:
    1. merge_two_sorted_sll(SLL([]).head, SLL([]).head) -> None
    2. merge_two_sorted_sll(SLL([1]).head, SLL([6]).head) -> SLL([1, 6]).head
    3. merge_two_sorted_sll(SLL([7, 9]).head, SLL([-11, 11]).head) -> SLL([-11, 7, 9, 11]).head
    4. merge_two_sorted_sll(SLL([-3, 14, 14]).head, SLL([-7, -6, 5]).head) -> SLL([-7, -6, -3, 5, 14, 14]).head
"""


def merge_two_sorted_sll(L1, L2):
    """Merges two singly linked lists into a sorted linked list.

    Args:
        n1 (Node): The head of one singly linked list.
        n2 (Node): The head of another singly linked list.

    Returns:
        Node: The head of sorted singly linked list.
    """

    # Creates a placeholder for the result.
    dummy_head = tail = Node(None)

    while L1 and L2:
        if L1._key < L2._key: tail._next, L1 = L1, L1._next
        else: tail._next, L2 = L2, L2._next
        tail = tail._next

    # Appends the remaining nodes of L1 or L2
    tail._next = L1 or L2
    return dummy_head._next


def merge_two_sorted_sll_rec(n1: Node, n2: Node) -> Node:
    """Merges two singly linked lists into a sorted linked list.

    Args:
        n1 (Node): The head of one singly linked list.
        n2 (Node): The head of another singly linked list.

    Returns:
        Node: The head of sorted singly linked list.
    """
    if not n1: return n2
    if not n2: return n1

    if n1._key < n2._key:
        n1._next = merge_two_sorted_sll_rec(n1._next, n2)
        return n1
    else:
        n2._next = merge_two_sorted_sll_rec(n1, n2._next)
        return n2


def main():
    functions = [merge_two_sorted_sll]
    for f in functions:
        # print(f"""{'*'*15} Running: {f.__name__} {'*'*15}""")
        for i in range(6):
            a = sorted([randint(-15, 15) for _ in range(i)])
            b = sorted([randint(-15, 15) for _ in range(i)])
            expected = sorted(a + b)

            sll1, sll2, sll_res = SLL(a), SLL(b), SLL()
            sll_res._head = f(sll1._head, sll2._head)

            returned = sll_res.keys()

            assert returned == expected

            # returned = f"""SLL({returned}).head""" if returned else None
            # ex = f"""{i+1}. {f.__name__}(SLL({a}).head, SLL({b}).head) -> {returned}"""
            # print(ex)


if __name__ == '__main__':
    main()
