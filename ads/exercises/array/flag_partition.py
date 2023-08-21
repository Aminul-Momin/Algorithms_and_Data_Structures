"""
Write a program that takes an array A and index i into A, and rearrange the
elements so that all elements less than A[i] appear first, followed by
elements equal to A[i], followed by elements greater than A[i].[- EPI: 5.1].
"""
#==============================================================================

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):

    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:left].
    # middle group: A[left:idx].
    # unclassified group: A[idx:right].
    # top group: A[right:].
    left, idx, right = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while idx < right:
        # A[idx] is the incoming unclassified element.
        if A[idx] < pivot:
            A[left], A[idx] = A[idx], A[left]
            left, idx = left + 1, idx + 1
        elif A[idx] == pivot:
            idx += 1
        else:  # A[idx] > pivot.
            right -= 1
            A[idx], A[right] = A[right], A[idx]
