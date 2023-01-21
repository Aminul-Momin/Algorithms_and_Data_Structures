import pytest

from ads.utils import load_json_data
from ads.exercises.mathematical import *

DATA = load_json_data("mathematical")


@pytest.mark.parametrize("k, expected", DATA["integer_square_root"])
def test_squre_root(k, expected):
    assert integer_square_root(k) == expected