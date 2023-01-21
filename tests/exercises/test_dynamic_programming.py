import pytest

from ads.utils import load_json_data
from ads.exercises.dynamic_programming import *

#==============================================================================
DATA = load_json_data('dynamic_programming')
#==============================================================================


# **************************** test_fib() ****************************** #
@pytest.mark.parametrize('n, expected', DATA["fib"])
def test_fib(n, expected):
    assert fib_rec(n) == expected
    assert fib_dp_tbl(n) == expected
    assert fib_dp_memo(n) == expected


# ********************** test_stairs_hop_ways() ************************ #
def test_stairs_hop_ways():
    for i in range(4, 50):
        tbl = stairs_3hop_tbl(i)
        memok = stairs_khop_memo(i, 3, {})

        assert memok == tbl

        # print(stairs_hop_3ways_tbl(i))
        # print(stairs_hop_kways_memo(i, 3))
        # print(stairs_hop_3ways_memo(i))


# ************************** test_can_sum() **************************** #
@pytest.mark.parametrize('target_sum, numbers, expected', DATA["can_sum"])
def test_can_sum(target_sum, numbers, expected):
    assert can_sum_rec(target_sum, numbers) == expected
    assert can_sum_memo(target_sum, numbers, {}) == expected
    assert can_sum_tbl(target_sum, numbers) == expected
    # print(f"""\ncan_sum({target_sum},{ numbers}) -> {expected}""")


# ************************** test_how_sum() **************************** #
@pytest.mark.parametrize('target_sum, numbers, expected', DATA["how_sum"])
def test_how_sum(target_sum, numbers, expected):

    assert how_sum_tbl(target_sum, numbers) == expected
    assert how_sum_rec(target_sum, numbers) == expected
    assert how_sum_memo(target_sum, numbers, {}) == expected


# ************************** test_best_sum() **************************** #
@pytest.mark.parametrize('target_sum, numbers, expected', DATA["best_sum"])
def test_best_sum(target_sum, numbers, expected):
    assert best_sum_tbl(target_sum, numbers) == expected
    assert best_sum_rec(target_sum, numbers) == expected
    assert best_sum_memo(target_sum, numbers, {}) == expected


# ************************ test_can_construct() *********************** #
@pytest.mark.parametrize('target, word_bank, expected', DATA["can_construct"])
def test_can_construct(target, word_bank, expected):
    assert can_construct_rec(target, word_bank) == expected
    assert can_construct_memo(target, word_bank, {}) == expected
    assert can_construct_tbl(target, word_bank) == expected


# ************************ test_count_construct() *********************** #
@pytest.mark.parametrize('target, word_bank, expected',
                         DATA["count_construct"])
def test_count_construct(target, word_bank, expected):
    assert count_construct_rec(target, word_bank) == expected
    assert count_construct_memo(target, word_bank, {}) == expected
    assert count_construct_tbl(target, word_bank) == expected


# ************************ test_all_construct() *********************** #
@pytest.mark.parametrize('target, word_bank, expected', DATA["all_construct"])
def test_all_construct_tbl(target, word_bank, expected):
    # print(f"""all_construct({target, word_bank}) -> {all_construct_tbl(target, word_bank)}\n""")
    assert all_construct_tbl(target, word_bank).sort() == expected.sort()

    # assert all_construct_memo(target, word_bank) == expected
    # assert all_construct_tbl(target, word_bank) == expected


# ************************ test_grid_traveler(m, n) ******************** #
@pytest.mark.parametrize('m, n, expected', DATA["grid_traveler"])
def test_grid_traveler(m, n, expected):
    assert grid_traveler_rec(m, n) == expected
    assert grid_traveler_memo(m, n) == expected
    assert grid_traveler_tbl(m, n) == expected
