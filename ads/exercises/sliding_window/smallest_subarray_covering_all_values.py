from ast import keyword
from collections import namedtuple
from typing import List

Subarray = namedtuple('Subarray', ('start', 'end'))
#==============================================================================
""" Find smallest subarray sequentially covering all values. - [EPI:12.8]

Write a program that takes two arrays of strings, and return the indices of
the starting and ending index of a shortest subarray of the first array
(`paragraph`) that "sequentially covers" the second array (`keywords`), i.e.,
contains all the strings in the second array (`keywords`), in the order in which
they appear in the (`keywords`) array.

- Example:
    - paragraph: [apple, banana, cat, apple]
    - keywords: [banana, apple]
    - You can assume all keywords are distinct.
    - The paragraph subarray starting at index `0` and ending at index `1` does not fulfill the requirements , eventhough it contains all the keywords, since they do not appear in the specified order.
    - the subarray starting at index `1` and ending at index `3` does fulfill the specification.

`NOTE`: According to the problem statement, sequential order needs to be maintained.

`Hint`: For each index in the paragraph array, compute the shortest subarray
ending at that index which fulfillsthe specification.
"""
#==============================================================================


def smallest_sequentially_covering_subset(paragraph, keywords) -> Subarray:

    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_lengths = [float('inf')] * len(keywords)
    shortest_len = float('inf')
    result = (-1, -1)

    for right, word in enumerate(paragraph):

        if word in keyword_to_idx:
            keyword_idx = keyword_to_idx[word]

            # Case-1: if `word` is first keyword in `keywords` list
            if keyword_idx == 0: shortest_lengths[keyword_idx] = 1

            # Case-2: `word` is not the first/last keyword in `keywords` list
            elif shortest_lengths[keyword_idx - 1] != float('inf'):

                # distance upto the imidiate previous keyword
                dist_upto_prev = shortest_lengths[keyword_idx - 1]

                # distance from the imidiate previous keyword to this `word`
                dist_from_prev = (right - latest_occurrence[keyword_idx - 1])

                # distance upto this keyword
                shortest_lengths[keyword_idx] = dist_upto_prev + dist_from_prev

            latest_occurrence[keyword_idx] = right


            # Case-3: if the `word` is last keyword in `keywords` list
            is_last_keyword = keyword_idx == len(keywords) - 1
            if (is_last_keyword and shortest_lengths[-1] < shortest_len):

                shortest_len = shortest_lengths[-1]
                result = (right - shortest_len + 1, right)

    return result[1] - result[0] + 1



def main():
    test_cases = [
        [["W", "T", "G", "V", "F", "D", "r", "l", "j", "N", "I"], ["T", "D"], 5],
        [["F", "G", "U", "S", "r", "r", "i", "X"], ["G", "U", "r"], 4],
        [["S", "O", "B"], ["S", "O", "B"], 3],
        [["x", "i", "W", "E"], ["W", "E"], 2],
        [["A", "g", "r", "C"], ["A", "C"], 4],
        [["h", "Q", "m", "h", "Q"], ["Q", "h"], 3],
        [["r", "T", "T"], ["r", "T"], 2],
        [["u", "F", "Q", "M", "o"], ["Q", "M"], 2],
        [["Y", "b", "c", "p", "u", "Z"], ["b", "p"], 3],
        [["p", "R", "n", "u", "A"], ["R", "A"], 4]]

    for paragraph, keywords, expected in test_cases:
        returned = smallest_sequentially_covering_subset(paragraph, keywords)
        assert returned == expected


if __name__ == '__main__':
    main()
