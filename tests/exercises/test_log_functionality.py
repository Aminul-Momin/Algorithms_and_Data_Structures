from random import randrange, randint, shuffle
import string
import pytest
import unittest

from ads.utils import load_json_data
from ads.exercises.array.arrayEPI_pvt import *
from ads.exercises.array import *

# ============================================================================
# ============================================================================

import logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler("logs/ads_log.log", mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


#==============================================================================
logger.info('Loading Json data for test_log_functionality')
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
