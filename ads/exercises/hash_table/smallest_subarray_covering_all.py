from collections import Counter, namedtuple
""" Find the smallest subarray covering all values - [EPI:12.7]

Write a program which takes an array of strings and a set of strings, and
retum the indices of the starting and ending index of a shortest subarray of
the given array that "covers" the set, i.e., contains all strings in the set.
Hint: rNhat is the maximum number of minimal subarrays that can cover the query?
"""

Subarray = namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):

    keywords_to_cover = Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result


def main():
    pass


if __name__ == '__main__':
    main()