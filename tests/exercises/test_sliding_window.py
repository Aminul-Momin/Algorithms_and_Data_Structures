import pytest
from ads.utils import load_json_data
from ads.exercises.sliding_window import *

DATA = load_json_data("sliding_window")


@pytest.mark.parametrize("L, k, expected", DATA["len_contegious_subarray"])
def test_len_contegious_subarray(L, k, expected):
    assert len_contegious_subarray(L, k) == expected


@pytest.mark.parametrize("L, k, expected",
                         DATA["smallest_sequentially_covering_subset"])
def test_smallest_sequentially_covering_subset(L, k, expected):
    assert smallest_sequentially_covering_subset(L, k) == expected
