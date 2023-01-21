import itertools, collections, random, heapq, operator, functools
"""[EPI: 24.2]"""


def find_first_missing_positive(A):

    # Record which values are present by writing A[i] to index A[i] - 1 if
    # A[i] is between 1 and len(A), inclusive. We save the value at index A[i]
    # - 1 by swapping it with the entry at i. If A[i] is negative or greater
    # than n, we just advance i.
    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i] - 1]:
            A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

    # Second pass through A to search for the first index i such that A[i] !=
    # i+1, indicating that i + 1 is absent. If all numbers between 1 and
    # len(A) are present, the smallest missing positive is len(A) + 1.
    return next((i + 1 for i, a in enumerate(A) if a != i + 1), len(A) + 1)


#==============================================================================
""" Test Justification. - [EPI: 24.8]

This problem is concerned with justifying text. It abstracts a problem arising
in typesetting. Theinput is specified as a sequence of words, and the target
line length. After justification, eachindividual line must begin with a word,
and each subsequent word must be separated from priorwords with at least one
blank. If a line contains more than one word, it should not end in a blank.
The sequences of blanks within each line should be as close to equal in length
as possible, with thelonger blank sequences, if any, appearing at the initial
part of the line. As an exception/ the verylast line should use single blanks
as separators, with additional blanks appearing at its end.For example ,if.
A = ("The", "ql)ick", "btown", "fox" , "jumped", "over", "the" , "lazy",
"dogs.")and the line length L is 1,1,, then the retumed result should be
"The---quick" , "brown---fox" ,"jumped-over" , "the- ---Lazy" , "dogs .
------". The symbol - denotes a blank.Write a program which takes as input an
array A of strings and a positive integer L, and computesthe justification of
the text specified by A.Hlnfr Solve it on a line-by-line basis, assuming a
single blank between pairs of words. Then figure out how todistribute excess
blanks.
"""
#==============================================================================


def justify_text(words, L):

    curr_line_length, result, curr_line = 0, [], []

    for word in words:
        if curr_line_length + len(word) + len(curr_line) > L:
            # Distribute equally between words in curr_line.
            for i in range(L - curr_line_length):
                curr_line[i % max(len(curr_line) - 1, 1)] += ' '

            result.append(''.join(curr_line))
            curr_line, curr_line_length = [], 0

        curr_line.append(word)
        curr_line_length += len(word)

    # Use ljust(L) to pad the last line with the appropriate number of blanks.
    return result + [' '.join(curr_line).ljust(L)]


#==============================================================================
""" Longest Increasing Subarray. - [EPI: 24.5]

An array is increasing if each element is less than its succeeding element
except for the last element. Implement an algorithm that takes as input an
array A of n elements, and returns the beginning and ending indices of
alongest increasing subarray of A. For example, lf A= (2,1,1,3,5,13,7,19,17,23),
the longest increasing subarray is (3,5, 13), and you should return (2,4).
Hint:lf A[il>Ali+ 1],insteadof checking Ali+71 <A[i+ 2],gofurtheroutinthearray.
"""
#==============================================================================

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A):

    result = Subarray(0, 0)
    i, max_length = 0, 1

    while i < len(A) - max_length:
        # Backward check and skip if A[j] >= A[j + 1].
        for j in range(i + max_length, i, -1):
            if A[j - 1] >= A[j]:
                i = j
                break
        else:  # Forward check if it is not skippable (the loop ended normally)
            i += max_length
            while i < len(A) and A[i - 1] < A[i]:
                i, max_length = i + 1, max_length + 1

            result = Subarray(i - max_length, i - 1)

    return result


"""[EPI: 24.7]"""


def rook_attack(A):

    m, n = len(A), len(A[0])
    has_first_row_zero = 0 in A[0]
    has_first_column_zero = any(not A[i][0] for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if not A[i][j]: A[i][0] = A[0][j] = 0

    for i in range(1, m):
        if not A[i][0]:
            for j in range(1, n):
                A[i][j] = 0

    for j in range(1, n):
        if not A[0][j]:
            for i in range(1, m):
                A[i][j] = 0

    if has_first_row_zero:
        for j in range(n):
            A[0][j] = 0

    if has_first_column_zero:
        for i in range(m):
            A[i][0] = 0


"""[EPI: 24.11]

Problem 8.3 on Page 102 defines matched strings of parens, brackets, and braces. This problemis restricted to strings of parens. Specifically, this problem is concerned with a long substrings ofmatched parens. As an example, if s is "((0)0(0(", then "(0)0" is a longest substring of matchedParens.Write a program that takes as input a string made up of the characters '(' and')', and returns thesize of a maximum length substring in which the parens are matched.Hint: Startwith a brute-force algorithm and then refine it by considering cases in which you can advance morequickly
"""


def longest_matching_parentheses(s):

    max_length, end, left_parentheses_indices = 0, -1, []
    for i, c in enumerate(s):
        if c == '(':
            left_parentheses_indices.append(i)
        elif not left_parentheses_indices:
            end = i
        else:
            left_parentheses_indices.pop()
            start = (left_parentheses_indices[-1]
                     if left_parentheses_indices else end)
            max_length = max(max_length, i - start)
    return max_length


def longest_matching_parentheses_constant_space(s):
    def parse_from_side(s, paren):
        max_length = num_parens_so_far = length = 0
        for c in s:
            if c == paren:
                num_parens_so_far, length = num_parens_so_far + 1, length + 1
            else:  # c != paren
                if num_parens_so_far <= 0:
                    num_parens_so_far = length = 0
                else:
                    num_parens_so_far -= 1
                    length += 1
                    if num_parens_so_far == 0:
                        max_length = max(max_length, length)
        return max_length

    return max(parse_from_side(s, '('), parse_from_side(reversed(s), ')'))


"""[EPI: 24.16]"""


def find_kth_in_two_sorted_arrays(A, B, k):

    # Lower bound of elements we will choose in A.
    b = max(0, k - len(B))
    # Upper bound of elements we will choose in A.
    t = min(len(A), k)

    while b < t:
        x = b + (t - b) // 2
        A_x_1 = float('-inf') if x <= 0 else A[x - 1]
        A_x = float('inf') if x >= len(A) else A[x]
        B_k_x_1 = float('-inf') if k - x <= 0 else B[k - x - 1]
        B_k_x = float('inf') if k - x >= len(B) else B[k - x]

        if A_x < B_k_x_1: b = x + 1
        elif A_x_1 > B_k_x: t = x - 1
        else:
            # B[k - x - 1] <= A[x] and A[x - 1] < B[k - x].
            return max(A_x_1, B_k_x_1)

    A_b_1 = float('-inf') if b <= 0 else A[b - 1]
    B_k_b_1 = float('-inf') if k - b - 1 < 0 else B[k - b - 1]
    return max(A_b_1, B_k_b_1)


"""[EPI: 24.17]"""


def find_kth_largest_unknown_length(stream, k):

    candidates = []
    for x in stream:
        candidates.append(x)
        if len(candidates) >= 2 * k - 1:
            # Reorders elements about median with larger elements appearing
            # before the median.
            find_kth_largest(k, candidates)
            # Resize to keep just the k largest elements seen so far.
            del candidates[k:]
    # Finds the k-th largest element in candidates.
    find_kth_largest(k, candidates)
    return candidates[k - 1]


# Pythonic solution that uses library method but costs O(nlogk) time.
def find_kth_largest_unknown_length_pythonic(stream, k):
    return heapq.nlargest(k, stream)[-1]


"""[EPI: 10.06]"""


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

        raise IndexError('no k-th node in array A')

    return find_kth(operator.gt)


# The numbering starts from one, i.e., if A = [3, 1, -1, 2] then
# find_kth_smallest(1, A) returns -1, find_kth_smallest(2, A) returns 1,
# find_kth_smallest(3, A) returns 2, and find_kth_smallest(4, A) returns 3.
def find_kth_smallest(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1:right + 1] contains elements that are
        # "less than" the pivot.
        #
        # Note: "greater than" and "less than" are defined by the comp object.
        #
        # Returns the new index of the pivot element after partition.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            # Generates a random integer in [left, right].
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1
        raise IndexError('no k-th node in array A')

    return find_kth(operator.lt)


""" Regular Expression matching. [EPI: 24.26]"""


def is_match(regex, s):
    def is_match_here(regex, s):
        if not regex:
            # Case (1.): Empty regex matches all strings.
            return True

        if regex == '$':
            # Case (2.): Reach the end of regex, and last char is '$'.
            return not s

        if len(regex) >= 2 and regex[1] == '*':
            # Case (3.): A '*' match.
            # Iterate through s, checking '*' condition, if '*' condition holds,
            # performs the remaining checks.
            i = 1
            while i <= len(s) and regex[0] in ('.', s[i - 1]):
                if is_match_here(regex[2:], s[i:]):
                    return True
                i += 1
            # See '*' matches zero character in s[:len(s)].
            return is_match_here(regex[2:], s)

        # Case (4.): regex begins with single character match.
        return bool(s and regex[0] in ('.', s[0])
                    and is_match_here(regex[1:], s[1:]))

    # Case (2.): regex starts with '^'.
    if regex[0] == '^':
        return is_match_here(regex[1:], s)
    return any(is_match_here(regex, s[i:]) for i in range(len(s) + 1))


"""[EPI: 24.31]"""


def max_subarray_sum_in_circular(A):

    # Calculates the non-circular solution.
    def find_max_subarray():
        maximum_till = maximum = 0
        for a in A:
            maximum_till = max(a, a + maximum_till)
            maximum = max(maximum, maximum_till)
        return maximum

    # Calculates the solution which is circular.
    def find_circular_max_subarray():
        def compute_running_maximum(A):
            partial_sum = A[0]
            running_maximum = [partial_sum]
            for a in A[1:]:
                partial_sum += a
                running_maximum.append(max(running_maximum[-1], partial_sum))
            return running_maximum

        # Maximum subarray sum starts at index 0 and ends at or before index i.
        maximum_begin = compute_running_maximum(A)
        # Maximum subarray sum starts at index i + 1 and ends at the last
        # element.
        maximum_end = compute_running_maximum(A[::-1])[::-1][1:] + [0]

        # Calculates the maximum subarray which is circular.
        return max(begin + end
                   for begin, end in zip(maximum_begin, maximum_end))

    return max(find_max_subarray(), find_circular_max_subarray())


"""[EPI: 24.33]"""


def max_rectangle_submatrix(A):

    MaxHW = collections.namedtuple('MaxHW', ('h', 'w'))
    # DP table stores (h, w) for each (i, j).
    table = [[None] * len(A[0]) for _ in A]

    for i, row in reversed(list(enumerate(A))):
        for j, v in reversed(list(enumerate(row))):
            # Find the largest h such that (i, j) to (i + h - 1, j) are feasible.
            # Find the largest w such that (i, j) to (i, j + w - 1) are feasible.
            table[i][j] = (MaxHW(
                table[i + 1][j].h +
                1 if i + 1 < len(A) else 1, table[i][j + 1].w +
                1 if j + 1 < len(row) else 1) if v else MaxHW(0, 0))

    max_rectangle_area = 0
    for i, row in enumerate(A):
        for j, v in enumerate(row):
            # Process (i, j) if it is feasible and is possible to update
            # max_rectangle_area.
            if v and table[i][j].w * table[i][j].h > max_rectangle_area:
                min_width = float('inf')
                for a in range(table[i][j].h):
                    min_width = min(min_width, table[i + a][j].w)
                    max_rectangle_area = max(max_rectangle_area,
                                             min_width * (a + 1))
    return max_rectangle_area


"""[EPI: 24.38]"""


def find_longest_subarray_less_equal_k(A, k):

    # Builds the prefix sum according to A.
    prefix_sum = list(itertools.accumulate(A))

    # Early returns if the sum of A is smaller than or equal to k.
    if prefix_sum[-1] <= k:
        return len(A)

    # Builds min_prefix_sum.
    min_prefix_sum = list(
        reversed(
            functools.reduce(lambda s, v: s + [min(v, s[-1])],
                             reversed(prefix_sum[:-1]), [prefix_sum[-1]])))
    a = b = max_length = 0
    while a < len(A) and b < len(A):
        min_curr_sum = (min_prefix_sum[b] -
                        prefix_sum[a - 1] if a > 0 else min_prefix_sum[b])
        if min_curr_sum <= k:
            curr_length = b - a + 1
            if curr_length > max_length:
                max_length = curr_length
            b += 1
        else:  # min_curr_sum > k.
            a += 1
    return max_length
