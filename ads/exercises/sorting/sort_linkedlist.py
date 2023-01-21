from ads.fundamentals import SLLNode as Node
#==============================================================================
""" Implement a fast sorting algorithm for lists. - [EPI:13.11]. """


def merge_two_sorted_lists(L1, L2):

    # Creates a placeholder for the result.
    dummy_head = tail = Node()

    while L1 and L2:
        if L1.data < L2.data: tail.next, L1 = L1, L1.next
        else: tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


def stable_sort_list(L):

    # Base cases: L is empty or a single node, nothing to do.
    if not L or not L.next: return L

    # Find the midpoint of L using a slow and a fast pointer.
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None  # Splits the list into two equal-sized lists.
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


def main():
    pass


if __name__ == '__main__':
    main()