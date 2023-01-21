import pytest
from ads.utils import *
from ads.exercises.linked_list import *
#==============================================================================
DATA = load_json_data('linked_list')
#==============================================================================


############################ nth_node_from_last ##############################
@pytest.mark.parametrize('a, nth, expected', DATA["nth_from_last"])
def test_nth_node_from_last(a, nth, expected):
    sll = SLL(a)
    res = nth_node_from_last(sll._head, nth)
    nth_item = res._key if res else None
    assert nth_item == expected


############################ Reverse a linked list ###########################
@pytest.mark.parametrize('a, expected', DATA["reverse_sll"])
def test_reverse_sll(a, expected):
    sll = SLL(a)
    sll._head = reverse_sll(sll._head)
    assert sll.keys() == expected


######################## Merege two sorted linked list #######################
@pytest.mark.parametrize('a, b, expected', DATA["merge_two_sorted_sll"])
def test_merge_two_sorted_sll(a, b, expected):
    sll1, sll2, sll = SLL(a), SLL(b), SLL()
    sll._head = merge_two_sorted_sll(sll1._head, sll2._head)
    assert sll.keys() == expected
