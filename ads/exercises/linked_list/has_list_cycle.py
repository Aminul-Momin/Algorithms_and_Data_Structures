from random import randrange, randint

from ads.fundamentals import SLL, SLLNode as Node
from ads.utils import yellow

#==============================================================================
"""
Write a function `has_cycle(head: Node)` which takes the head of a singly
linked list and returns `None` if there does not exist a cycle, and the node
at the start of the cycle, if a cycle is present.

NOTE: You don not know the length of the list in advance.
"""
#==============================================================================

# TESTING IS NOT DONE YET !!
def has_cycle(head: Node) -> Node:
    """Finds the head of the cycle in the given linked list.

    Args:
        head (Node): The head of the given linked list.

    Returns:
        Node: Head of the cycle if there is one, None otherwise.
    """
    def count_cycle_len(cycle_head: Node) -> int:
        """Count the number of nodes in the given cycle

        Args:
            cycle_head (Node): The head node of the cycle

        Returns:
            int: The total number of nodes int the given cycle.
        """
        current, counter = cycle_head, 0
        while True:
            counter += 1
            current = current._next
            if current is cycle_head:
                return counter

    fast = slow = head

    while fast and fast._next and fast._next._next:
        slow, fast = slow._next, fast._next._next

        if slow is fast:
            # Finds the starting node of the cycle:
            # (step-1): place second pointer at `length-of-cycle` steps ahead of head.
            second = head
            for _ in range(count_cycle_len(slow)):
                second = second._next

            first = head
            # (step-2): now make first and second pointers iterate in tendem.
            # second pointer is 'length-of-cycle' steps ahead of first pointer.
            while first is not second:
                first = first._next
                second = second._next

            return first  # since now first pointer at the starting of cycle.

    return None  # No cycle.


def main():
    functions = [has_cycle]
    L = []

    for f in functions:
        print(f"""{'*'*15} {yellow('Running')}: {f.__name__} {'*'*15}""")
        for i in range(70):
            a = [randint(-15, 15) for _ in range(i)]

            expected = None

            sll = SLL(a)
            sll._head = f(sll._head)
            returned = None if not sll.keys() else sll.keys()
            assert expected == returned

            # returned = f"""SLL({returned}).head""" if returned else None
            # ex = f"""{i}. {f.__name__}(SLL({a}).head, {m}, {n}) -> {returned}"""
            # print(ex)
            # L.append([a, m, n, returned])

    # print(L)


if __name__ == '__main__':
    main()
