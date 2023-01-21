from random import randrange
import unittest
import os

from ads.searching.sequential_search_st import SequentialSearchST
from ads.utils import *


class TestSequentialSearchST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = "Algorithms_and_Data_Structures/data/shellsST.txt"
        cls.DATA_FILE_PATH = os.path.abspath(os.path.join(os.pardir, data))

        cls.kvp = {
            10001: "Chelsea",
            10003: "Lower East Side",
            10004: "Lower Manhattan",
            10010: "Gramercy Park",
            10012: "Soho",
            10021: "Upper East Side",
            10023: "Upper West Side",
            10029: "East Harlem",
        }

        cls.T1 = SequentialSearchST()
        cls.T2 = SequentialSearchST()
        load_data_from_file(cls.DATA_FILE_PATH, cls.T1)
        load_data_from_collection(cls.kvp, cls.T2)

    @classmethod
    def tearDownClass(cls):
        print("\nteardownClass")
        for key in cls.T1.keys():
            cls.T1.delete(key)
        assert cls.T1.is_empty()
        cls.T1 = None

    # def setUp(self):
    #     print('setUp')
    #     self.T3 = SequentialSearchST()
    #     self.assertTrue(self.T3.is_empty())

    # def tearDown(self):
    #     print('tearDown\n')
    #     self.T3 = None

    def test_size(self):
        self.assertEqual(self.T1.size(), 7)
        self.assertEqual(self.T2.size(), len(self.kvp))

    def test_is_empty(self):
        self.assertFalse(self.T1.is_empty())
        self.assertFalse(self.T2.is_empty())

    def test_contains(self):
        self.assertTrue("by", self.T1)
        self.assertTrue("she", self.T1)

        self.assertNotIn("bye", self.T1)
        self.assertNotIn(1003, self.T2)

        self.assertTrue(10003, self.T2)
        self.assertTrue(10004, self.T2)

        with self.assertRaises(ValueError):
            self.T2.contains(None)
            self.T1.contains(None)

    def test_get(self):
        self.assertEqual(self.T1.get("by"), 4)
        self.assertEqual(self.T1.get("she"), 0)

        self.assertIsNone(self.T2.get(1003))

        self.assertEqual(self.T2.get(10001), "Chelsea")
        self.assertEqual(self.T2.get(10003), "Lower East Side")
        self.assertEqual(self.T2.get(10004), "Lower Manhattan")
        self.assertEqual(self.T2.get(10029), "East Harlem")

        with self.assertRaises(ValueError):
            self.T1.get(None)
            self.T2.get(None)

    def test_put(self):
        self.T2.put(10040, "Washington Heights")
        self.assertIn(10040, self.T2)
        self.assertEqual(self.T2.get(10040), "Washington Heights")
        self.assertEqual(self.T2.size(), len(self.kvp) + 1)

        with self.assertRaises(ValueError):
            self.T1.put(None, randrange(0, 11))
            self.T2.put(None, randrange(0, 11))

        self.T2.delete(10040)

    def test_delete(self):
        self.T2.delete(10001)
        self.assertNotIn(10001, self.T2)
        self.assertEqual(self.T2.size(), len(self.kvp) - 1)

        self.T2.delete(10029)
        self.assertNotIn(10029, self.T2)
        self.assertEqual(self.T2.size(), len(self.kvp) - 2)

        with self.assertRaises(ValueError):
            self.T1.delete(None)
            self.T2.delete(None)

        self.T2.put(10001, "Chelsea")
        self.T2.put(10029, "East Harlem")


if __name__ == "__main__":
    unittest.main()
