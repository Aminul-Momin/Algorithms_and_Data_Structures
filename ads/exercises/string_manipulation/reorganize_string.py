from random import randint, choice
import heapq
import string
from collections import Counter
#==============================================================================
""" Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

- Example 1:
    - Input: s = "aab"
    - Output: "aba"

- Example 2:
    - Input: s = "aaab"
    - Output: ""
 

- Constraints:
    1) 1 <= s.length <= 500
    2) s consists of lowercase English letters.
"""


def reorganize_str(s):
    counts = Counter(s)
    result = []

    max_pq = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_pq)

    while len(max_pq) > 1:
        cur_count, cur_char = heapq.heappop(max_pq)
        nxt_count, nxt_char = heapq.heappop(max_pq)

        result.append(cur_char)
        result.append(nxt_char)

        counts[cur_char] = counts[cur_char] - 1
        counts[nxt_char] = counts[nxt_char] - 1

        if counts[cur_char] > 0:
            heapq.heappush(max_pq, (-counts[cur_char], cur_char))
        if counts[nxt_char] > 0:
            heapq.heappush(max_pq, (-counts[nxt_char], nxt_char))
    if max_pq:
        last_count, last_char = heapq.heappop(max_pq)
        if counts[last_char] > 1: return ''
        result.append(last_char)

    return ''.join(result)


def validate(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]: return False
    return True


def main():
    s = ''.join([choice(list(string.ascii_uppercase)) for _ in range(50)])
    returned = reorganize_str(s)
    assert validate(returned)
    print(f" Given: {s} \n Returned: {returned}")


if __name__ == '__main__':
    main()
