"""Find the length of a longest contained interval. - [EPI:12.10].

Write a program which takes as input a set of integers represented by an 
array, and retums the size of a largest subset of integers in the array
having the property that if two integers are in the subset, then so are all
integers between them.
For example, if the input is {3, -2, 7, 9, 8, 7, 2, 0, -1, 5, 8}, the largest
such subset is {-2, -1, 0, 1, 2, 3}, so you should retum 6.

Hint:Do you really need a total ordering on the input?
"""


def longest_contained_range(A):

    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Finds the lower bound of the largest range containing a.
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Finds the upper bound of the largest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size,
                                upper_bound - lower_bound - 1)
    return max_interval_size


def main():
    pass


if __name__ == '__main__':
    main()