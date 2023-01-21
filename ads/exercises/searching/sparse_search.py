from typing import List
#==============================================================================
""" Find string from list of strings with interspreded empyt strings. [CtCI: 11.5].

    Write a function 'find_string_from_strings(L, s)' which takes as input a
    sorted list of strings which is interspreaded with empyt strings and a
    string 's' and returns the index of 's' in the given list.

    Examples:
        1. find_string_from_strings([], "Texas") -> -1
        2. find_string_from_strings(["","","",""], "b") -> -1
        3. find_string_from_strings(["a","","","","tea","up",""], "up") -> 5
        4. find_string_from_strings(["a","","a","","","","b","b","b"], "b")  -> 6
"""


def find_string_from_strings(L: List[str], s: str) -> int:
    if not s or len(L) == 0: return -1
    low, high = 0, len(L) - 1

    while low <= high:
        mid = (low + high) // 2
        if not L[mid]:
            left, right = mid - 1, mid + 1

            while True:
                if left < low and right > high: return -1
                elif left >= low and L[left]:
                    mid = left
                    break
                elif right <= high and L[right]:
                    mid = right
                    break
                left -= 1
                right += 1

        if s < L[mid]: high = mid - 1
        elif s > L[mid]: low = mid + 1
        else: return mid
