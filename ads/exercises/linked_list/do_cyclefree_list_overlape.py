from random import randint
from ads.fundamentals import SLLNode as Node, SLL

#==============================================================================
#==============================================================================


def is_cyclefree_list_overlapping(head1, head2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    head1_len, head2_len = length(head1), length(head2)

    if head2_len < head1_len:
        smaller, larger = head2, head1  # head2 is the longer list

    # Advances the longer list to get equal length lists.
    for _ in range(abs(head1_len - head2_len)):
        larger = larger.next

    while smaller and larger and smaller is not larger:
        smaller, larger = smaller.next, larger.next

    return smaller  # None implies there is no overlap between smaller and larger.


def main():
    pass


if __name__ == '__main__':
    main()
