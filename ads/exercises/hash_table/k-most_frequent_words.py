""" Top K Frequent Words. - [EPI: 12.5]

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

- Example 1:
  - Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
  - Output: ["i", "love"]
  - Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.
- Example 2:
  - Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
  - Output: ["the", "is", "sunny", "day"]
  - Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.
- Note:
  - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
  - Input words contain only lowercase letters.
- Follow up:
  - Try to solve it in O(n log k) time and O(n) extra space.
"""
#==============================================================================

from ads.utils import gen_list_of_words
from random import randint
import os

def top_k_frequent_words(words, k):
    """ Returns the top k frequent words in a list of words.

    Args:
        words (list[str]): List of words.
        k (int): Number of top frequent words to return.

    Returns:
        list[str]: List of top k frequent words.
    """
    # Create a dictionary of word counts.
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Create a list of tuples of (word, count) sorted by count.
    word_count_tuples = []
    for word, count in word_counts.items():
        word_count_tuples.append((word, count))
    word_count_tuples.sort(key=lambda x: x[1], reverse=True)

    # Return the top k words.
    return [word for word, count in word_count_tuples[:k]]

def main():
    test_cases = [
        gen_list_of_words(randint(10, 20), word_file_name='shellsST.txt') for _ in range(10)
    ]
    for test_case in test_cases:
        # print(test_case)
        print(top_k_frequent_words(test_case, randint(1, 5)))

if __name__ == '__main__':
    main()
