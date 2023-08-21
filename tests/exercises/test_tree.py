from random import sample, randint
import pytest

from ads.exercises.tree import *
from ads.utils import gen_bst, load_json_data
#==============================================================================
DATA = load_json_data("tree")
#==============================================================================


# @pytest.mark.parametrize("L, expected", DATA["height_bt"])
# def test_height_bt(L, expected):
#     bst = gen_bst(L)
#     assert height_bt_v1(bst._root) == expected
#     assert height_bt_v2(bst._root) == expected + 1


@pytest.mark.parametrize("L, expected", DATA["width_bt"])
def test_width_bt(L, expected):
    bst = gen_bst(L)
    assert width_bt(bst._root) == expected


# @pytest.mark.parametrize("L, expected", DATA["count_leaves"])
# def test_count_leaves(L, expected):
#     bst = gen_bst(L, type=AVL)
#     assert count_leaves(bst._root) == expected

# def test_tree():
#     A = []
#     for i in range(10):
#         L = [randint(-5,5) for _ in range(i)]
#         bst = gen_bst(L)
#         # print("\n",bst)
#         res = width_bt(bst._root)
#         A.append([L, res])
#         print(f"""width_bt(gen_bst({L})._root) -> {res}""")
# print(A)
