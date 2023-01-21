from random import randint, randrange
#==============================================================================
""" Compute the intersection of two sorted arrays. - [EPI:13.1]. """


def A_intersection_B(A, B):
    a, b, aAndB = 0, 0, []

    while a < len(A) and b < len(B):
        if A[a] < B[b]: a += 1
        elif A[a] > B[b]: b += 1
        elif (a == 0 or A[a - 1] != A[a]):  # A[a] == B[b] and A[a-1] != A[a]
            aAndB.append(A[a])
            a, b = a + 1, b + 1
        else:
            b += 1  # A[a] == B[b] and A[a-1] == A[a]

    return aAndB


# Returns the intersection of this set and that set.
def intersects(this, that):
    if that is None: raise ValueError("invalid argument !")
    c = set()
    if len(this) < len(that):
        for x in this:
            if x in that: c.add(x)
    else:
        for x in that:
            if x in this: c.add(x)
    return c


def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and a in B]


def main():
    for _ in range(1000):
        N, M = randrange(0, 50), randrange(0, 50)
        A = sorted([randint(-10, 10) for _ in range(N)])
        B = sorted([randint(-10, 10) for _ in range(M)])
        L1, L2 = intersect_two_sorted_arrays(A, B), A_intersection_B(A, B)
        assert L1 == L2


if __name__ == '__main__':
    main()
