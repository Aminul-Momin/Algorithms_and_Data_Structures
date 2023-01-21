import pytest

from ads.exercises.string_manipulation.string_manipulation_pvt import *
from ads.exercises.string_manipulation import *
from ads.utils import *

DATA = load_json_data("string_manipulation")

##############################################################################
##############################################################################


###################### Interconvert String and Integer #######################
@pytest.mark.parametrize("string, integer", DATA["interconvert_str_int"])
def test_interconversion_v1(string, integer):
    assert str_to_int_v1(string) == integer
    assert str_to_int_v2(string) == integer
    assert str_to_int_v3(string) == integer

    assert int_to_str_v1(integer) == string
    assert int_to_str_v2(integer) == string


def test_interconversion_v2():
    for i in range(1000):
        _int = randint(-5000, 5001)
        _str = str(_int)
        assert str_to_int_v1(_str) == _int
        assert str_to_int_v2(_str) == _int
        assert str_to_int_v3(_str) == _int

        assert int_to_str_v1(_int) == _str
        assert int_to_str_v2(_int) == _str
