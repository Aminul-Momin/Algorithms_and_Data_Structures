from random import randint
from typing import List

from ads.heaps.priority_queue import PriorityQueue
from ads.fundamentals import SLLNode as Node, SLL

#==============================================================================
""" Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
        [ 1->4->5, 1->3->4, 2->6 ]
    merging them into one sorted list:
        1->1->2->3->4->4->5->6


Example 2:

    Input: lists = []
    Output: []
    Example 3:

    Input: lists = [[]]
    Output: []
 

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length won't exceed 10^4.
"""
#==============================================================================

#==============================================================================
""" Approach 1: Brute Force:

        Intuition & Algorithm

        Traverse all the linked lists and collect the values of the nodes into an array.
        Sort and iterate over this array to get the proper value of nodes.
        Create a new sorted linked list and extend it with the new nodes.

        Complexity Analysis

        Time complexity : O(N logN) where N is the total number of nodes.

        Collecting all the values costs O(N) time.
        A stable sorting algorithm costs O(NlogN) time.
        Iterating for creating the linked list costs O(N) time.
        Space complexity : O(N).

        Sorting cost O(N) space (depends on the algorithm you choose).
        Creating a new linked list costs O(N) space.
"""
#==============================================================================

def mergeKLists(lists: List[SLL]) -> Node:

    nodes = []
    head = point = Node(0)
    for sll in lists:
        while sll:
            nodes.append(sll._key)
            sll = sll._next
    
    for x in sorted(nodes):
        point._next = Node(x)
        point = point._next
    
    return head._next


""" Approach 2: Compare one by one
        Compare every k nodes (head of every linked list) and get the node with the smallest value.
        Extend the final sorted linked list with the selected nodes.

        Time complexity : O(kN) where k is the number of linked lists.
            Almost every selection of node in final linked costs O(k) (k-1 times comparison).
            There are N nodes in the final linked list.
        
        Space complexity :
            O(n) Creating a new linked list costs O(n) space.
            O(1) It's not hard to apply in-place method - connect selected nodes instead of creating new nodes to fill the new linked list.
"""

#==============================================================================
"""
Approach 3: Optimize Approach 2 by Priority Queue

    Time complexity : O(Nlogk) where k is the number of linked lists.

        - The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
        -There are N nodes in the final linked list.
    
    Space complexity :
        O(n) Creating a new linked list costs O(n) space.
        O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).
"""
#==============================================================================
def merge_k_lists_v2(lists: List[SLL]) -> Node:
    head = point = Node(0)
    q = PriorityQueue()

    for sll in lists:
        if sll: q.put((sll._key, sll))

    while not q.empty():
        val, node = q.get()
        point._next = Node(val)
        point = point._next
        node = node._next
        if node:
            q.put((node._key, node))
    return head._next

#==============================================================================
"""
Approach 5: Merge with Divide And Conquer:
    This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly

    - Pair up k lists and merge each pair.
    - After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
    - Repeat this procedure until we get the final sorted linked list.

    Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about log2k times.

    Time complexity : O(Nlogk) where k is the number of linked lists.
        - We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
        - Sum up the merge process and we can get: O(Nlogk)
    
    Space complexity :
        We can merge two sorted linked lists in O(1) space.
"""
#==============================================================================


def merge_k_lists_v3(lists: List[SLL]) -> Node:
    
    def _merge2Lists(l1, l2):
        
        head = point = Node(0)

        while l1 and l2:
            if l1._key <= l2._key:
                point._next = l1
                l1 = l1._next
            else:
                point._next = l2
                l2 = l1
                l1 = point._next._next
            point = point._next

        if not l1: point._next = l2

    amount = len(lists)
    
    interval = 1
    
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = _merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    
    return lists[0] if amount > 0 else None


def main():
    pass


if __name__ == '__main__':
    main()
