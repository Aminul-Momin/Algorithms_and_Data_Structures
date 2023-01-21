from collections import namedtuple
#==============================================================================
""" Compute the union of intervals. - [EPI:13.8]. """

Endpoint = namedtuple('Endpoint', ('is_closed', 'val'))
Interval = namedtuple('Interval', ('left', 'right'))


def is_overlaped(first, second):
    if (first.left.val < second.right.val
            or (first.left.val == second.right.val and
                (first.left.is_closed or second.right.is_closed))):
        return (first.right.val > second.right.val
                or (first.right.val == second.right.val
                    and first.right.is_closed))
    return False


def union_of_intervals_v2(intervals):

    # Empty input.
    if not intervals: return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if intervals and is_overlaped(i, result[-1]):
            result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    return result


def main():
    pass


if __name__ == '__main__':
    main()
