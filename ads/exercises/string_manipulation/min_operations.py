
##### [2937. Make Three Strings Equal](https://leetcode.com/problems/make-three-strings-equal/description/)


from collections import deque

def min_operations_iterative(s1, s2, s3):
    """
    Finds the minimum number of operations to make three strings equal by deleting
    rightmost characters iteratively.

    Args:
      s1: The first string.
      s2: The second string.
      s3: The third string.

    Returns:
      The minimum number of operations required, or -1 if impossible.
    """

    queue = deque([(s1, s2, s3, 0)])
    visited = set()

    while queue:
        s1, s2, s3, count = queue.popleft()

        if s1 == s2 == s3: return count

        if (s1, s2, s3) in visited: continue

        visited.add((s1, s2, s3))

        if len(s1) > 1: queue.append((s1[:-1], s2, s3, count + 1))
        if len(s2) > 1: queue.append((s1, s2[:-1], s3, count + 1))
        if len(s3) > 1: queue.append((s1, s2, s3[:-1], count + 1))

    return -1

def min_operations(s1, s2, s3):
    """
    Finds the minimum number of operations to make three strings equal by deleting
    rightmost characters.

    Args:
      s1: The first string.
      s2: The second string.
      s3: The third string.

    Returns:
      The minimum number of operations required, or -1 if impossible.
    """

    def is_equal(s1, s2, s3):
        return s1 == s2 and s2 == s3

    def backtrack(s1, s2, s3, count):
        if is_equal(s1, s2, s3): return count

        if len(s1) == 1 and len(s2) == 1 and len(s3) == 1 and not is_equal(s1, s2, s3): return -1

        min_ops = float('inf')
        if len(s1) > 1: min_ops = min(min_ops, backtrack(s1[:-1], s2, s3, count + 1))
        if len(s2) > 1: min_ops = min(min_ops, backtrack(s1, s2[:-1], s3, count + 1))
        if len(s3) > 1: min_ops = min(min_ops, backtrack(s1, s2, s3[:-1], count + 1))

        return min_ops

    return backtrack(s1, s2, s3, 0)

