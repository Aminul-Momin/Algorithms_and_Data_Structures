
"""
 +--------------+-------------------------------------------------------------+
 | Execution:   | $ python3 substring_search.py                               |
 +--------------+-------------------------------------------------------------+
 | Dependencies:| None                                                        |
 +--------------+-------------------------------------------------------------+

    $ python3 substring_search.py
        0
        0
        10
        10
        75
        75
        1354
        1354
        1183
        1183
        1464
        1464
"""


def substring_search_brute_force(pattern, text):
    """ Return the index in text where the given pattern matches.
    """
    N, M, i = len(text), len(pattern), 0

    for i in range((N-M)+1):
        j = 0
        while j < M:
            if pattern[j] != text[i+j]:
                break
            j += 1
        if j == M:
            return i     # index in text where pattern starts
    return N                    # Pattern not found


# Brute-force substring search: alternate implementation. Brute-force algorithm
# can be slow if text and pattern are repetitive. Worst case. ~ M N char compares.
# Same sequence of char compares as previous implementation.
#   * i points to end of sequence of already-matched chars in text.
#   * j stores number of already-matched chars (end of sequence in pattern).

def substring_search_brute_force_X(pattern, text):
    """ Return the index in text where the given pattern matches.
    """
    N, M, i, j = len(text), len(pattern), 0, 0

    while i < N and j < M:
        if pattern[j] == text[i]:
            j += 1
        else:
            i -= j              # explicit backup
            j = 0
        i += 1
    if j == M:
        return i - M     # index in text where pattern starts
    return N                    # Not found

###########################################################################
########################### Client of the class: ##########################


def test_substring_search():
    text = "GAATTGCTAGCAATTGCTAGCAATTGCTAGCAATTCAACCAGATCACCGAAAACTGTCCTCCAAAT\
        CCCTCACACTCCCAAATTCGCGGGCTTCTGCCTCTTAGACCACTCTACCCTATTCCCCACACTCACCGGA\
        CCAAAGCCGCGGCCCTTCCGTTTCTTTGCTTTTGAAAGACCCCACCCGTAGGTGGCAAGCTAGCTTAAGT\
        ACGCCACTTTGCAAGGCATGGAAAAATACATAACTGAGAATAGGAAAGTTCAGATCAAGGTCAGGAACAA\
        GAAACAGCTGAATACCAAACAGGATATCTGTGGTAAGCGGTTCCTGCCCCGGCTCAGGGCCAAGAACAGA\
        GAGACAGCTGAGTGATGGGCCAAACAGGATATCTGTGGTAAGCAGTTCCTGCCCCGGCTCGGGGCCAAGA\
        CAGATGGTCCCCAGATGCGGTCCAGCCCTCAGCAGTTTCTAGTGAATCATCAGATGTTTCCAGGGTGCCC\
        AAGGACCTGAAAATGACCCTGTACCTTATTTGAACTAACCAATCAGTTCGCTTCTCGCTTCTGTTCGCGC\
        CTTCCGCTCTCCGAGCTCAATAAAAGAGCCCACAACCCCTCACTCGGCGCGCCAGTCTTCCGATAGACTG\
        GTCGCCCGGGTACCCGTATTCCCAATAAAGCCTCTTGCTGTTTGCATCCGAATCGTGGTCTCGCTGTTCC\
        TGGGAGGGTCTCCTCTGAGTGATTGACTACCCACGACGGGGGTCTTTCATTTGGGGGCTCGTCCGGGATT\
        GGAGACCCCTGCCCAGGGACCACCGACCCACCACCGGGAGGTAAGCTGGCCAGCAACTTATCTGTGTCTG\
        CCGATTGTCTAGTGTCTATGTTTGATGTTATGCGCCTGCGTCTGTACTAGTTAGCTAACTAGCTCTGTAT\
        TGGCGGACCCGTGGTGGAACTGACGAGTTCTGAACACCCGGCCGCAACCCTGGGAGACGTCCCAGGGACT\
        TGGGGGCCGTTTTTGTGGCCCGACCTGAGGAAGGGAGTCGATGTGGAATCCGACCCCGTCAGGATATGTG\
        TTCTGGTAGGAGACGAGAACCTAAAACAGTTCCCGCCTCCGTCTGAATTTTTGCTTTCGGTTTGGAACCG\
        AGCCGCGCGTCTTGTCTGCTGCAGCATCGTTCTGTGTTGTCTCTGTCTGACTGTGTTTCTGTATTTGTCT\
        AAAATTAGGGCCAGACTGTTACCACTCCCTTAAGTTTGACCTTAGGTCACTGGAAAGATGTCGAGCGGAT\
        GCTCACAACCAGTCGGTAGATGTCAAGAAGAGACGTTGGGTTACCTTCTGCTCTGCAGAATGGCCAACCT"

    words = ["GAATT", "CAATTGCTA", "CCTCAC", "AGTTTGAC", "AACCT", "CAACCT"]
    for i in range(len(words)):
        # print(substring_search_brute_force(words[i], text) == \
        #       substring_search_brute_force_X(words[i], text))
        print(substring_search_brute_force(words[i], text))
        print(substring_search_brute_force_X(words[i], text))


if __name__ == '__main__':
    test_substring_search()

###########################################################################
