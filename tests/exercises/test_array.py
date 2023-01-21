from random import randrange, randint, shuffle
import string
import pytest
import unittest

from ads.utils import load_json_data
from ads.exercises.array.arrayEPI_pvt import *
from ads.exercises.array import *
#==============================================================================
DATA = load_json_data('array')
#==============================================================================


############################# Delete Duplicates ##############################
@pytest.mark.parametrize("P, expected", DATA["delete_duplicates"])
def test_delete_duplicates(P, expected):
    delete_duplicates(P)
    assert P == expected


def test_delete_duplicates_v2():
    for i in range(10):
        L = sorted([randint(1, 5) for _ in range(i)])
        A, B = list(L), list(L)
        assert delete_duplicates(A) == delete_duplicates_pythonic(B)


################################## Plus One ##################################
class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):

        self.assertListEqual(plus_one([0]), [1])
        self.assertListEqual(plus_one([9]), [1, 0])
        self.assertListEqual(plus_one([1, 0, 9]), [1, 1, 0])
        self.assertListEqual(plus_one([9, 9, 8, 0, 0, 9]), [9, 9, 8, 0, 1, 0])
        self.assertListEqual(plus_one([9, 9, 9, 9]), [1, 0, 0, 0, 0])


##############################  Stock Buy-Sell  ##############################
class TestBuySellStockOnce(unittest.TestCase):
    def setUp(self):
        self.P = [randrange(0, 9) for _ in range(15)]
        self.k = randrange(len(self.P) * 3)
        # prof_k = buy_and_sell_k_times(P, k)

    @pytest.mark.skip(reason='It is implemented by the author')
    def test_buy_sell_once(self):
        one_sell_profit = buy_sell_once(self.P)
        k_sell_profit = buy_and_sell_k_times(self.P, 1)
        self.assertEqual(one_sell_profit, k_sell_profit)

    def test_buy_sell_once(self):
        one_sell_profit = buy_sell_once(self.P)
        k_sell_profit = buy_and_sell_k_times(self.P, 1)
        self.assertEqual(one_sell_profit, k_sell_profit)


class TestBuySellStockTwice(unittest.TestCase):
    def setUp(self):
        self.P = [randrange(0, 9) for _ in range(15)]
        self.k = randrange(len(self.P) * 3)
        # prof_k = buy_and_sell_k_times(P, k)

    def test_buy_sell_twice(self):
        two_sell_profit = buy_sell_twice(self.P)
        k_sell_profit = buy_and_sell_k_times(self.P, 2)
        self.assertEqual(two_sell_profit, k_sell_profit)

    def test_buy_sell_twice_v2(self):
        two_sell_profit = buy_sell_twice_v2(self.P)
        k_sell_profit = buy_and_sell_k_times(self.P, 2)
        self.assertEqual(two_sell_profit, k_sell_profit)


def test_buy_sell_once():
    P = [randrange(0, 9) for _ in range(15)]
    one_sell_profit = buy_sell_once(P)
    k_sell_profit = buy_and_sell_k_times(P, 2)
    assert one_sell_profit == k_sell_profit


def test_buy_sell_once_v2():
    P = [randrange(0, 9) for _ in range(15)]
    one_sell_profit = buy_sell_once_v2(P)
    k_sell_profit = buy_and_sell_k_times(P, 2)
    assert one_sell_profit == k_sell_profit


def test_buy_sell_twice():
    P = [randrange(0, 9) for _ in range(15)]
    two_sell_profit = buy_sell_twice(P)
    k_sell_profit = buy_and_sell_k_times(P, 2)
    assert two_sell_profit == k_sell_profit


def test_buy_sell_twice_v2():
    P = [randrange(0, 9) for _ in range(15)]
    two_sell_profit = buy_sell_twice_v2(P)
    k_sell_profit = buy_and_sell_k_times(P, 2)
    assert two_sell_profit == k_sell_profit


#############################  Apply Permutation  ############################
@pytest.mark.parametrize("A, P, expected", DATA["apply_permutation"])
def test_apply_permutation_v1(A, P, expected):
    apply_permutation_v1(A, P)
    assert A == expected


def test_apply_permutation():
    for _ in range(1000):
        A0, A_size = [], randrange(5, 10)

        while True:
            alphabet = string.ascii_uppercase[randint(0, 25)]
            if alphabet not in A0: A0.append(alphabet)
            if len(A0) == A_size: break

        A = list(A0)
        shuffle(A)

        P = [A.index(a) for a in A0]
        apply_permutation_v1(A0, P)
        assert A0 == A


##############################  Next Permutation #############################


@pytest.mark.parametrize("P, expected", DATA["next_permutation"])
def test_next_permutation_v1(P, expected):
    next_permutation_v1(P)
    assert P == expected


##############################  Generate Primes ##############################
@pytest.mark.parametrize("n, expected", DATA["generate_primes"])
def test_generate_primes_v1(n, expected):
    assert generate_primes_v1(n) == expected


@pytest.mark.parametrize("n, expected", DATA["generate_primes"])
def test_generate_primes_v2(n, expected):
    assert generate_primes_v2(n) == expected
