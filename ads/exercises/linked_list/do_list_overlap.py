from random import randint
from ads.fundamentals import SLLNode as Node, SLL
from ads.exercises.linked_list import *


#==============================================================================
def overlapping_lists(l0, l1):

    # Store the start of cycle if any.
    root0, root1 = has_cycle(l0), has_cycle(l1)

    if not root0 and not root1:
        # Both lists are cycles free.
        return is_cyclefree_list_overlapping(l0, l1)
    elif (root0 and not root1) or (not root0 and root1):
        # One list has cycle, one list has no cycle.
        return None

    # Both lists have cycles.
    temp = root1
    while True:
        temp = temp.next
        if temp is root0 or temp is root1:
            break

    # l0 and l1 do not end in the same cycle.
    if temp is not root0:
        return None  # Cycles are disjoint.

    # Calculates the distance between a and b.
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    # l0 and l1 end in the same cycle, locate the overlapping node if they
    # first overlap before cycle starts.
    stem0_length, stem1_length = distance(l0, root0), distance(l1, root1)
    if stem0_length > stem1_length:
        l1, l0 = l0, l1
        root0, root1 = root1, root0
    for _ in range(abs(stem0_length - stem1_length)):
        l1 = l1.next
    while l0 is not l1 and l0 is not root0 and l1 is not root1:
        l0, l1 = l0.next, l1.next

    # If l0 == l1 before reaching root0, it means the overlap first occurs
    # before the cycle starts; otherwise, the first overlapping node is not
    # unique, we can return any node on the cycle.
    return l0 if l0 is l1 else root0
