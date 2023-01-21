'''
Write a function 'all_construct(target, word_bank)' that accepts a target string
and an aarray of strings.

The function should return a 2D array containing all of the ways taht the
'target' can be constructed by concatenating elements of the 'word_bank' array.
Each element of the 2D array should represent one combination that constructs
the 'target'.

You may reuse elements of 'word_bank' as many times as needed.
'''
#==============================================================================
from ads.utils import *
#==============================================================================

def all_construct_tbl(target, word_bank):
    tbl = [[[]]] + [[] for _ in range(len(target))]
    N = len(tbl)

    for i in range(N):
        for word in word_bank:
            if i + len(word) < N and target[i:i+len(word)] == word:
                combs = [subarray + [word] for subarray in tbl[i]]
                tbl[i + len(word)] += combs
                # for subarray in combs: tbl[i+len(word)].append(subarray)

    return tbl[-1]




def main():
    test_cases = load_json_data('dynamic_programming')['all_construct']
    for target, word_bank, expected in test_cases:
        actual = all_construct_tbl(target, word_bank)
        assert actual.sort() == expected.sort()


if __name__ == '__main__':
    main()
