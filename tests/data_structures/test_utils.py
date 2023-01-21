import unittest, pytest
from random import *

from ads.utils import *

DATA = load_json_data('utils')


@pytest.mark.parametrize("a, low, high, expected", DATA["reverse"])
def test_reverse(a, low, high, expected):
    if len(a) == 0 or low < 0 or high >= len(a):
        with pytest.raises(IndexError):
            reverse(a, low, high)
    else:
        reverse(a, low, high)
        assert a == expected


@pytest.mark.parametrize("a, rotate_amount, expected", DATA["rotate_right"])
def test_rotate_right(a, rotate_amount, expected):
    rotate_list(a, rotate_amount)
    assert a == expected
