"""
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

- Example 1:
    - Input: s = "ADOBECODEBANC", t = "ABC"
    - Output: "BANC"
    - Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
- Example 2:
    - Input: s = "a", t = "a"
    - Output: "a"
    - Explanation: The entire string s is the minimum window.
- Example 3:
    - Input: s = "a", t = "aa"
    - Output: ""
    - Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
 

- Constraints:
    - m == s.length
    - n == t.length
    - 1 <= m, n <= 105
    - s and t consist of uppercase and lowercase English letters.
 

- Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

#==============================================================================
"""
Minimum Window Substring
Given a string corpus and a string target, find the minimum window (substring) which contain all the characters that are found in target.

The time complexity of the solution should be in order of O(n).


NOTE: substring and  sub-sequence are different things


- Example 1:
    - Input: corpus = "donutsandwafflemakemehungry"  target = "flea"
    - Output: "affle" or "flema"

- Example 2:
    - Input: corpus = "whoopiepiesmakemyscalegroan"  target = "roam"
    - Output: "myscalegro"

- Example 3:
    - Input: corpus = "coffeeteabiscuits"  target = "cake"
    - Output: ""
    - Explanation: since the letter k is not found in the corpus, a minimum window cannot be found.
"""
#==============================================================================

import collections
from collections import Counter
import sys


def min_window_v1(s: str, t: str):
    if not t or not s: return ""
    cnt_ptrn_chrs = Counter(t)  # Counts of Pattern Characters
    req_len = len(cnt_ptrn_chrs)  # Number of required lenght

    left, right = 0, 0  # left and right pointer
    curr_len = 0
    cnt_win_chrs = {}  # Counts of Window Characters

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    for right, char in enumerate(s):

        # Add one character from the right to the window
        cnt_win_chrs[char] = cnt_win_chrs.get(char, 0) + 1

        if char in cnt_ptrn_chrs and cnt_win_chrs[char] == cnt_ptrn_chrs[char]:
            curr_len += 1

        # Try and contract the window till it ceases to be 'desirable'.
        while (left <= right) and (curr_len == req_len):
            char = s[left]

            # Save the smallest window until now.
            if right - left + 1 < ans[0]: ans = (right - left + 1, left, right)

            # s[left] is no longer a part of the window.
            cnt_win_chrs[char] -= 1
            if char in cnt_ptrn_chrs and cnt_win_chrs[char] < cnt_ptrn_chrs[
                    char]:
                curr_len -= 1

            # increment left pointer to look for a new shrunk window.
            left += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


def min_window_v2(s, t):

    if not t or not s: return ""

    cnt_ptrn_chrs = Counter(t)

    req_len = len(cnt_ptrn_chrs)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in cnt_ptrn_chrs: filtered_s.append((i, char))

    left = 0
    cur_len = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    for right, char in enumerate(filtered_s):
        character = filtered_s[right][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == cnt_ptrn_chrs[character]:
            cur_len += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while left <= right and cur_len == req_len:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[right][0]
            start = filtered_s[left][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < cnt_ptrn_chrs[character]:
                cur_len -= 1
            left += 1

        right += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


def min_window_v3(searchString, t):
    left = 0
    right = 0

    # It stores the length of maximum valid substring
    minimum = sys.maxsize
    counter_t = collections.Counter(t)
    counter_search = collections.defaultdict(int)
    count = 0
    minimum_window = ""

    # Here we use the 2 pointers approach
    while right < len(searchString):
        counter_search[searchString[right]] += 1
        if searchString[right] in counter_t:
            if counter_search[searchString[right]] <= counter_t[searchString[right]]:
                count += 1

        while left <= right and count == len(t):
            if minimum > right - left + 1:
                minimum = right - left + 1
                minimum_window = searchString[left:right + 1]

            counter_search[searchString[left]] -= 1
            if searchString[left] in counter_t and counter_search[searchString[left]] < counter_t[searchString[left]]:
                count -= 1

            left += 1

        right += 1

    return minimum_window


def min_window_brute_force(searchString, t):
    # Helper function to check if all the char of string are
    # Present in the string searchString
    def contains_all(searchString, t):
        required_characters = {}

        for i in range(0, len(t)):
            occurrences = 0
            if t[i] in required_characters:
                occurrences = required_characters[t[i]]

            required_characters[t[i]] = occurrences + 1

        for i in range(0, len(searchString)):
            curr = searchString[i]

            if curr in required_characters:
                # Calculate what the new occurrence count will be
                new_occurrences = required_characters[curr] - 1
                """
                If we have satisfied all of the characters for this character, remove the key
                from the hashtable.

                Otherwise, just update the mapping with 1 less occurrence to satisfy for
                """

                if new_occurrences == 0:
                    del required_characters[curr]
                else:
                    required_characters[curr] = new_occurrences
        """
        If we satisfied all characters the the required characters hashtable will be
        empty
        """
        return not required_characters



    n = len(searchString)

    # It contains the min length seen so far
    min_window_size = sys.maxsize

    # It contains the minimum length substring
    min_window = ""

    # The nested for loop help us generate all the substrings
    for left in range(0, n):
        for right in range(left, n):

            # Generate the substring
            window_snippet = searchString[left:right + 1]

            # Check if the generated char contains all the characters of target
            window_contains_all = contains_all(window_snippet, t)

            # If it is a valid substring
            # And the length is less than the minimum so far
            # Update the answer
            if window_contains_all and len(
                    window_snippet) < min_window_size:
                min_window_size = len(window_snippet)
                min_window = window_snippet

    return min_window


def min_window_v4(s: str, t: str):

    keywords_to_cover = Counter(t)
    res = (-1, -1)
    remaining_to_cover = len(keywords_to_cover)
    idx_left = 0

    for idx_right, word in enumerate(s):
        if word in t:
            keywords_to_cover[word] -= 1
            if keywords_to_cover[word] == 0: remaining_to_cover -= 1

        while remaining_to_cover == 0:
            length = res[1] - res[0]
            if length == 0 or length > idx_right - idx_left:
                res = (idx_left, idx_right)

            win_left_chr = s[idx_left]
            if win_left_chr in t:
                keywords_to_cover[win_left_chr] += 1
                if keywords_to_cover[win_left_chr] > 0: remaining_to_cover += 1
            idx_left += 1

    return "" if res == (-1, -1) else s[res[0]:res[1] + 1]


def main():
    test_cases = [["ADOBECODEBANC", "ABC", "BANC"], ["a", "a", "a"],
                  ["aa", "aa", "aa"], ["a", "aa", ""]]
    for text, pattern, expected in test_cases:
        assert min_window_v3(text, pattern) == expected

if __name__ == '__main__':
    main()
