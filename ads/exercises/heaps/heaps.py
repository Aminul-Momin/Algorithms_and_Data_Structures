from random import randint, randrange
import heapq
from typing import List
from collections import namedtuple
#==============================================================================
""" Sort an INCREASTNG-DECREASTNG array.

An array is said to be k-increasing-decreasing if elements repeatedly increase up to a certain indexafter which they decrease, then again increase, a total of k times.
"""
#==============================================================================




#==============================================================================
""" Sort an almost sorted array.

Write a Program which takes as input a very long sequence of numbers and prints the numbers insorted order. Each number is at most k away from its correctly sorted position. (Such an array issometimesreferredtoasbeingk-sorted.) Forexample,nonumberinthesequence(3, -1.,2,6,4,5,8>is more than 2 away from its final sorted position.Hint: f{ow many numbers must you read after reading the ith number to be sure you can place it in the correct location?
"""
#==============================================================================


#==============================================================================
""" Computes the k-closest stars.

Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points,and assume distances are in light years. The Milky Way consists of approximately 1012 stars, and their coordinates are stored in a file.
How would you compute the k stars which are closest to Earth?
"""
#==============================================================================


#==============================================================================
""" Compute the median of online data.

You want to compute the running median of a sequence of numbers. The sequence is presented to you in a streaming fashion, you cannot back up to read an earlier value, and you need to output the median after reading in each new element.
For example, if the input is 1, 0, 3, 5, 2, 0, 1, the output is 1, 0.5, 1, 2, 2, 1.5, 1.
Design an algorithm for computing the running median of a sequence.Hint: Avoid looking at all values each time you read a new value.
"""
#==============================================================================


#******************************************************************************
#************************** Collected Problems ********************************
#******************************************************************************

#==============================================================================
""" 
Given k sorted arrays, merge them into one sorted array. [ByteByByte]
"""
#==============================================================================


class PQNode:
    def __init__(self, a_idx: int, idx: int, value: int):
        self.a_idx = a_idx
        self.idx = idx
        self.value = value

    def __lt__(self, other_pq_node):
        return self.value < other_pq_node.value

    def __gt__(self, other_pq_node):
        return self.value > other_pq_node.value


PQNode = namedtuple('PQNode', ('value', 'cur_list', 'idx'))


def merge_k_lists(lists: List[List]):
    pq = []
    heapq.heapify(pq)

    for i, array in enumerate(lists):
        if len(array) > 0: heapq.heappush(pq, PQNode(array[0], i, 0))

    res_list = []

    while pq:
        node = heapq.heappop(pq)
        res_list.append(node.value)
        next_idx = node.idx + 1
        if next_idx < len(lists[node.cur_list]):
            heapq.heappush(
                pq,
                PQNode(lists[node.cur_list][next_idx], node.cur_list,
                       next_idx))
    return res_list


def merge_k_arrays(arrays: List[List]):
    size = 0
    pq = []
    heapq.heapify(pq)

    for i, array in enumerate(arrays):
        size += len(array)
        if len(array) > 0: heapq.heappush(pq, PQNode(array[0], i, 0))

    idx = 0
    res_array = [None] * size
    len_pq = len(pq)

    while pq and idx < size:
        node = heapq.heappop(pq)
        res_array[idx] = node.value
        next_idx = node.idx + 1
        if next_idx < len(arrays[node.cur_list]):
            heapq.heappush(
                pq,
                PQNode(arrays[node.cur_list][next_idx], node.cur_list,
                       next_idx))
            len_pq += 1
        idx += 1
    return res_array


def main():
    list_of_sorted_lists = [
        sorted([randint(-99, 99) for _ in range(randint(0, 5))])
        for _ in range(randint(2, 5))
    ]
    returned = merge_k_arrays(list_of_sorted_lists)
    expected = [*heapq.merge(*list_of_sorted_lists)]
    assert returned == expected


if __name__ == '__main__':
    main()
