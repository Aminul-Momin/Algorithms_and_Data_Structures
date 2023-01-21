import builtins
import collections

from random import randint
try:
    # assumed 'ads' is installed from PyPI into running environment
    from ads.fundamentals import SLLNode, SLL
except (ImportError):
    # assumed data structures of 'ads' are imported into ece.utils.py somehow
    from ece.utils import SLLNode, SLL
#==============================================================================
"""
Write an function named 'sunset_view(buildings)' that processes buildings with
height in east-to-west order and return the set of buildings which view the
sunset

Examples:

"""


def sunset_view(sequence):

    Building = collections.namedtuple('Building', ('id', 'height'))
    stk = []  # list of candidates

    for idx, height in enumerate(sequence):
        while stk and height >= stk[-1].height:
            stk.pop()
        stk.append(Building(idx, height))

    return [c.height for c in stk]


def main():
    for i in range(7):
        buildings = [randint(1, 15) for _ in range(i)]
        res = sunset_view(buildings)
        ex = f"""sunset_view({buildings}) -> {res}"""
        print(ex)


if __name__ == '__main__':
    main()
