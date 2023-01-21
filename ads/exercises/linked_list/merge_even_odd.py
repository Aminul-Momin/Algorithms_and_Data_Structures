from random import randint, randrange

from ads.fundamentals import SLLNode as Node, SLL
#==============================================================================
""" Even Odd Linked List

Given the head of a singly linked list, group all the nodes with Even indices
together followed by the nodes with odd indices, and return the reordered list.

The first node is considered Even, and the second node is odd, and so on.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]
 
Constraints:
    n == number of nodes in the linked list
    0 <= n <= 104
    -106 <= Node.val <= 106
"""


def even_odd_merge(L):

    if not L:
        return L

    even_dummy_head, odd_dummy_head = Node(0), Node(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1  # Alternate between even and odd.

    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next


def main():
    pass


if __name__ == '__main__':
    main()