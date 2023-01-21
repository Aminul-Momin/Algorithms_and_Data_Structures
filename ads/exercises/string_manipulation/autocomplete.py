from ads.utils.utils import load_data_from_file
from random import randint
from typing import List, Dict
#==============================================================================


def autocomplete(word_bank: List[str], prefix: str) -> List[str]:
    class Node:
        def __init__(self, prefix):
            self._prefix: str = prefix
            self._children: Dict[chr, Node] = {}
            self._is_word: bool = False

    def insert_word(word: str) -> None:
        current = tri_root

        for i, char in enumerate(word):
            if not current._children.get(char):
                current._children[char] = Node(word[0:i + 1])
            current = current._children[char]
        current._is_word = True

    def words_with_prefix(prefix: str) -> List[str]:
        def find_prefixed_words(n: Node) -> None:
            if n._is_word: prefixed_words.append(n._prefix)
            for char in n._children.keys():
                find_prefixed_words(n._children.get(char))

        prefixed_words = []
        current = tri_root
        for char in prefix:
            if char not in current._children: return prefixed_words
            current = current._children[char]

        find_prefixed_words(current)
        return prefixed_words

    tri_root = Node('')
    for word in word_bank:
        insert_word(word)
    return words_with_prefix(prefix)


def autocomplete_v2(word_bank: List[str], prefix: str) -> List[str]:
    class Node:
        def __init__(self, char):
            self._char = char
            self._children = {}
            self._is_word = False

    def insert_word(word: str) -> None:
        current = tri_root

        for char in word:
            if not current._children.get(char):
                current._children[char] = Node(char)
            current = current._children[char]
        current._is_word = True

    def words_with_prefix(prefix: str) -> List[str]:
        def find_prefixed_words(n: Node, word) -> None:
            if n._is_word: prefixed_words.append(word)
            for char in n._children.keys():
                find_prefixed_words(n._children.get(char), word + char)

        prefixed_words = []
        current = tri_root
        for char in prefix:
            if char not in current._children: return prefixed_words
            current = current._children[char]

        find_prefixed_words(current, prefix)
        return prefixed_words

    tri_root = Node('')
    for word in word_bank:
        insert_word(word)
    return words_with_prefix(prefix)


def main():
    word_bank = load_data_from_file('shellsST.txt', [])
    prefix = 'sh'
    returned = autocomplete_v2(word_bank, prefix)

    print(word_bank, returned, sep='->')


if __name__ == '__main__':
    main()
