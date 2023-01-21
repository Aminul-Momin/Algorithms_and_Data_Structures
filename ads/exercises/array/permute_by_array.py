from ads.utils import swap
#==============================================================================
""" Apply a permutation to a given array. - [EPI: 5.10].

    Given an array A of n distince elements and a permutation array P, apply P to A. 

    Examples:
        apply_permutation(["A", "B"], [1, 0])   ->  ["B", "A"]
        apply_permutation(["A", "B", "C"], [0, 2, 1])   ->  ["A", "C", "B"]
        apply_permutation(["A","B","C","D"], [2,0,1,3])   -> ["B","C","A","D"]
        apply_permutation(["A","B","C","D"], [3,2,1,0]   -> ["D","C","B","A"]
        apply_permutation(["A", "B", "C", "D", "E"], [4, 0, 3, 1, 2])   -> ["B", "D", "E", "C", "A"]
"""


def apply_permutation(perm, A):

    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
    # Restore perm.
    perm[:] = [a + len(perm) for a in perm]


def apply_permutation2(perm, A):
    ''' BUGY CODE !!! '''
    L = [True] * len(A)

    for i, truthy in enumerate(L):
        if truthy:
            starting_idx = i
            next_idx = perm[i]
            swap(A, i, perm[starting_idx])
            L[i] = False

            while (next_idx != starting_idx):
                next_idx = perm[next_idx]
                swap(A, i, next_idx)
                L[next_idx] = False


def apply_permutation_v1(A, P):

    for i in range(len(A)):
        next = i
        while P[next] >= 0:
            A[i], A[P[next]] = A[P[next]], A[i]
            tmp = P[next]
            P[next] -= len(P)
            next = tmp

    for i in range(len(P)):
        P[i] += len(P)
