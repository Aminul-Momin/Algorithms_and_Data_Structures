from random import *
import unittest
import pytest

from ads.exercises.searching.searching_pvt import *
from ads.exercises.searching import *
from ads.utils import load_json_data, yellow


@pytest.fixture(scope='module')
def data():
    return load_json_data('searching')

DATA = load_json_data('searching')


@pytest.mark.parametrize("L, k, expected", DATA["first_idx_of_k_itr"])
def test_search_first_of_k(L, k, expected):
    assert search_first_of_k(L, k) == expected


@pytest.mark.parametrize("L, expected", DATA["magic_index_itr"])
def test_magic_index(L, expected):
    assert magic_index(L) == expected


@pytest.mark.parametrize("L, expected", DATA["magic_index_v2"])
def test_magic_index_v2(L, expected):
    assert magic_index_v2(L) == expected


@pytest.mark.skip
@pytest.mark.parametrize("L, expected", DATA["search_smallest"])
def test_search_first_of_k(L, expected):
    assert search_smallest(L) == expected

@pytest.mark.xfail
@pytest.mark.parametrize("L, expected", DATA["search_smallest"])
def test_search_smallest_v2(L, expected):
    assert search_smallest_v2(L) == expected


@pytest.mark.parametrize("L, key, expected", DATA["find_rotated_sorted"])
def test_find_rotated_sorted_rec(L, key, expected):
    assert find_rotated_sorted_rec(L, key) == expected


def test_rotated_sorted_rec():
    for i in range(100):
        N = randint(10, 20)
        L = sorted([randint(-10, 10) for _ in range(N)])
        key = choice(L) if L else None
        res = rotated_sorted_rec(L, key, 0, len(L) - 1)
        res2 = find_rotated_sorted_rec(L, key)
        assert res == res2
        # print("Index:", res, "key:", key)

        if res != -1: assert key == L[res]
        else: assert key not in L and len(L) == 0


@pytest.mark.parametrize("L, s, expected", DATA["find_string_from_strings"])
def test_find_string_from_strings(L, s, expected):
    assert find_string_from_strings(L, s) == expected


class TestBinarySearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.L0 = [[[*range(5)], 2, 2], [[5, 4, 3, 2], 5, 0], [[0], 1, -0.0],
                  [[1, 3, 6, 9], 9, 3]]

    def setUp(self):
        r = randrange(0, 1000)
        self.L1 = [[[*range(5)], 2, 2], [[5, 4, 3, 2], 5, 0], [[0], 1, -0.0],
                   [[1, 3, 6, 9], 9, 3]]
        self.k = choice([*range(-10, 10)])
        print(self.L1)

    # @pytest.mark.parametrize("L, k, expected", self.L0)
    # def test_search_first_of_k(self, L, k, expected):
    #     assert search_first_of_k(L, k) == expected

    # def test_idx_k_rec(self):
    #     self.assertEqual(self.k, self.L[idx_k_rec(
    #         self.L, self.k, 0, len(self.L)-1)])

    # def test_idx_k_nearnest(self):
    #     self.assertEqual(self.k, self.L[idx_k_nearest(self.L, self.k)])

    # def test_idx_k_nearest_rec(self):
    #     self.assertEqual(self.k, self.L[idx_k_nearest_rec(
    #         self.L, self.k, 0, len(self.L)-1)])

    def tearDown(self):
        pass
