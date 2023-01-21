import pytest

from ads.exercises.recursion import *
from ads.utils import load_json_data
# from ece.recursion.all_recursion import n_choose_k

DATA = load_json_data('recursion')

############################  Permutation Testing  ###########################


@pytest.mark.parametrize('permutable, expected', DATA["permute_str_v1"])
def test_permute_str_v1(permutable, expected):
    assert permute_str_v1(permutable) == expected


@pytest.mark.parametrize('permutable, expected', DATA["permute_str_v2"])
def test_permute_str_v2(permutable, expected):
    assert permute_str_v2(permutable) == expected


@pytest.mark.parametrize('permutable, expected', DATA["permute_str_v3"])
def test_permute_str_v3(permutable, expected):
    assert permute_str_v3(permutable) == expected


@pytest.mark.parametrize('permutable, expected', DATA["permute_list_v1"])
def test_permute_list_v1(permutable, expected):
    assert permute_list_v1(permutable) == expected


@pytest.mark.parametrize('permutable, expected', DATA["permute_list_v2"])
def test_permute_list_v2(permutable, expected):
    assert permute_list_v2(permutable) == expected


@pytest.mark.parametrize('permutable, expected', DATA["permute_list_v3"])
def test_permute_list_v3(permutable, expected):
    assert permute_list_v3(permutable) == expected


############################  Power Set Testing  #############################
@pytest.mark.parametrize('permutable, expected', DATA["power_set_list_v1"])
def test_power_set_list_v1(permutable, expected):
    assert power_set_list_v1(permutable) == expected


# @pytest.mark.parametrize('permutable, expected', DATA["power_set_str_v2"])
# def test_power_set_str_v2(permutable, expected):
#     assert power_set_str_v2(permutable) == expected


@pytest.mark.parametrize('permutable, expected', DATA["power_set_str_v3"])
def test_power_set_str_v3(permutable, expected):
    assert power_set_str_v3(permutable) == expected


###########################  Combination Testing  ############################
@pytest.mark.parametrize('str1, k, expected', DATA["combination"])
def test_comb_str_v1(str1, k, expected):
    assert comb_str_v1(str1, k) == expected


@pytest.mark.parametrize('str1, k, expected', DATA["combination"])
def test_comb_str_v2(str1, k, expected):
    assert comb_str_v2(str1, k) == expected


@pytest.mark.parametrize('str1, k, expected', DATA["combination"])
def test_comb_list_v1(str1, k, expected):
    assert comb_list_v1(str1, k) == expected


@pytest.mark.parametrize('str1, k, expected', DATA["combination"])
def test_comb_list_v2(str1, k, expected):
    assert comb_list_v2(str1, k) == expected


@pytest.mark.parametrize('N, k, expected', DATA["n_choose_k"])
def test_n_choose_k(N, k, expected):
    assert n_choose_k(N, k) == expected


############################  N-Chose-K Testing  #############################

#######################  Generate Parenthesis Testing  #######################

#############################  N-Queens Testing  #############################
