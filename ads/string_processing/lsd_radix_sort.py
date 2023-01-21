import sys, os
from random import randint, randrange


class LSD(object):
    """ Least Significant Digit Radix sort implementations.

    This class provides sort method for string with same length of extended
    ASCII characters using Least Significant Digit Radix sort.
    """

    RADIX = 256  # Extended ASCII alphabet size

    def __init__(self):
        pass

    def sort(self, a):
        N = len(a)
        d = len(a[0]) - 1
        aux = [0] * N

        for d in range(d, -1):
            count = [0] * (LSD.RADIX + 1)
            for i in range(N):  # computes frequency-count
                r = ord(a[i][d])
                count[r + 1] += 1
            for i in range(1, LSD.RADIX):  # transform counts into indices
                count[i] += count[i - 1]
            for i in range(N):  # distributes
                r = ord(a[i][d])
                aux[count[r]] = a[i]
                count[r] += 1
            for i in range(N):  # copy back
                a[i] = aux[i]


#############################  Utility Functions ##############################


def isSorted(array):
    for i in range(len(array) - 1, 0, -1):
        if array[i] < array[i - 1]:
            return False
    return True


def read_data_file(file, queue):
    with open('words.txt', "r") as f:
        for line in f.readlines():
            for word in line.split():
                queue.append(word)


def test_LSD(*args):
    cs = LSD()
    L = []
    if args: read_data_file(args, L)
    else: read_data_file('words.txt', L)
    cs.sort(L)
    print('Is the given list sorted: ', isSorted(L))
    print(L)


###############################################################################

if __name__ == '__main__':
    if len(sys.argv) > 1: test_LSD(sys.argv[1])
    else: test_LSD()
