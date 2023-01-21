from collections import Counter
#==============================================================================
""" Compute all string decompositions. - [EPI:12.12].

This problem is concered with taking a string (the "sentence" string) and a
set of strings (the"words"), and finding the substrings of the sentence which
are the concatenation of all the words(in any order).
 - Example:
 if the sentence string is "a man a plan a canal" and the set of words is
 ["can","apl", "ana"], "aplanacan" is a substring of the sentence that is the
 concatenation of all words.

Write a program which takes as input a string (the "sentence") and an array
of shings (the "words"),and retums the starting indices of substrings of the
sentence string which are the concatenation of all the strings in the words
array. Each string must appear exactly once, and their ordering is immaterial.
Assume all strings in the words array have equal length. It is possible for
the words array to contain duplicates.

Hint: Exploit the fact that the words have the same length.
"""


def find_all_substrings(s, words):
    def match_all_words_in_dict(start):
        curr_string_to_freq = Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_freq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                # curr_word occurs too many times for a match to be possible.
                return False
        return True

    word_to_freq = Counter(words)
    unit_size = len(words[0])
    return [
        i for i in range(len(s) - unit_size * len(words) + 1)
        if match_all_words_in_dict(i)
    ]


def main():
    pass


if __name__ == '__main__':
    main()