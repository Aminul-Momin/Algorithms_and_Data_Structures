import unittest
from random import randrange
import os

from ads.utils import NUMBERS, load_data_from_file, load_data_from_collection
from ads.searching.bst_st import BinarySearchTreeST


class TestBinarySearchTreeST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.DATA_FILE_NAME = "shellsST.txt"

    def setUp(self):
        self.kvp = NUMBERS

        self.T1 = BinarySearchTreeST()
        self.T2 = BinarySearchTreeST()

        load_data_from_file(self.DATA_FILE_NAME, self.T1)
        load_data_from_collection(self.kvp, self.T2)

    def tearDown(self):
        for key in self.T1.keys():
            self.T1.delete(key)
        assert self.T1.is_empty()
        self.T1 = None

    def test_size(self):
        self.assertEqual(self.T1.size(), 7)
        self.assertEqual(self.T2.size(), len(self.kvp))

    def test_is_empty(self):
        self.assertFalse(self.T1.is_empty())
        self.assertFalse(self.T2.is_empty())

    def test_contains(self):
        self.assertIn("by", self.T1)
        self.assertIn("she", self.T1)
        self.assertNotIn("bye", self.T1)  # ≠ self.assertFalse('bye', self.T1)

        self.assertNotIn("APPLE", self.T2)  # ≠ self.assertFalse(1003, self.T2)

        self.assertIn("ZERO", self.T2)
        self.assertIn("FIFTY", self.T2)

        with self.assertRaises(ValueError):
            self.T2.contains(None)
            self.T1.contains(None)

    def test_get(self):
        self.assertEqual(self.T1.get("by"), 4)
        self.assertEqual(self.T1.get("she"), 0)

        self.assertIsNone(self.T2.get("APPLE"))

        self.assertEqual(self.T2.get("ZERO"), 0)
        self.assertEqual(self.T2.get("THIRTY"), 30)
        self.assertEqual(self.T2.get("TWENTY"), 20)
        self.assertEqual(self.T2.get("FIFTY"), 50)

        with self.assertRaises(ValueError):
            self.T1.get(None)
            self.T2.get(None)

    def test_put(self):
        self.T2.put("EIGHTY", 80)
        self.assertIn("EIGHTY", self.T2)
        self.assertEqual(self.T2.get("EIGHTY"), 80)
        self.assertEqual(self.T2.size(), len(self.kvp) + 1)

        with self.assertRaises(ValueError):
            self.T1.put(None, randrange(0, 11))
            self.T2.put(None, randrange(0, 11))

        self.T2.delete("EIGHTY")

    def test_delete(self):
        self.T2.delete("ZERO")
        self.assertNotIn("ZERO", self.T2)
        self.assertEqual(self.T2.size(), len(self.kvp) - 1)

        self.T2.delete("THIRTY")
        self.assertNotIn("THIRTY", self.T2)
        self.assertEqual(self.T2.size(), len(self.kvp) - 2)

        with self.assertRaises(ValueError):
            self.T1.delete(None)
            self.T2.delete(None)

        self.T2.put("ZERO", 0)
        self.T2.put("THIRTY", 30)

    def test_select(self):
        self.assertEqual(self.T2.select(0), "FIFTY")
        self.assertEqual(self.T2.select(3), "THIRTY")

        T3 = BinarySearchTreeST()
        with self.assertRaises(ValueError):
            self.T2.select(-1)
            self.T2.select(8)
            T3.select(-1)

    def test_rank(self):
        self.assertEqual(self.T2.rank("APPLE"), 0)  # key not in tree
        self.assertEqual(self.T2.rank("FIFTY"), 0)
        self.assertEqual(self.T2.rank("FORTY"), 1)
        self.assertEqual(self.T2.rank("ZERO"), len(self.kvp) - 1)
        self.assertEqual(self.T2.rank("ZEROO"),
                         len(self.kvp))  # key not in tree
        self.assertEqual(self.T2.rank("ZZERO"),
                         len(self.kvp))  # key not in tree

        T3 = BinarySearchTreeST()
        with self.assertRaises(ValueError):
            self.T2.rank(None)
            T3.rank(None)

    def test_keys_inrange(self):
        # key not in tree
        # self.assertEqual(self.T2.keys_inrange(10001, 10029), 7)
        self.assertEqual(self.T2.keys_inrange("APPLE", "ZERO"), [])
        self.assertEqual(self.T2.keys_inrange("FIFTY", "FIFTY"), ["FIFTY"])
        self.assertEqual(self.T2.keys_inrange("FIFTY", "FORTY"), ["FIFTY"])
        self.assertEqual(self.T2.keys_inrange("FORTY", "FIFTY"), [])

        T3 = BinarySearchTreeST()
        with self.assertRaises(ValueError):
            self.T2.keys_inrange(None, None)
            T3.keys_inrange(10001, None)
            T3.keys_inrange(None, 10003)

    def test_size_inrange(self):
        self.assertEqual(self.T2.size_inrange("FIFTY", "ZERO"), len(self.kvp))
        self.assertEqual(self.T2.size_inrange("APPLE", "FIFTY"), 1)
        self.assertEqual(self.T2.size_inrange("FIFTY", "APPLE"), 0)
        self.assertEqual(self.T2.size_inrange("ZERO", "ZERO"), 1)
        self.assertEqual(self.T2.size_inrange("ZERO", "ZZERO"), 1)
        self.assertEqual(self.T2.size_inrange("TWENTY", "ZERO"), 2)

        T3 = BinarySearchTreeST()
        with self.assertRaises(ValueError):
            self.T2.size_inrange(None, None)
            T3.size_inrange(10001, None)

    def test_keys(self):
        keys_inorder = [key for key in self.kvp.keys()]
        keys_inorder.sort()
        self.assertEqual(self.T2.keys(), keys_inorder)

    def test_keys_level_order(self):
        keys = ["ZERO", "TEN", "FORTY", "TWENTY", "FIFTY", "THIRTY"]
        self.assertEqual(self.T2.keys_level_order(), keys)

    def test_checked(self):
        self.assertTrue(self.T1.checked())
        self.assertTrue(self.T2.checked())

        T3 = BinarySearchTreeST()
        self.assertTrue(T3.checked())

    def test_is_BST(self):
        self.assertTrue(self.T1.is_BST())
        self.assertTrue(self.T2.is_BST())

        T3 = BinarySearchTreeST()
        self.assertTrue(T3.is_BST())

    def test_is_size_consistent(self):
        self.assertTrue(self.T1.is_size_consistent())
        self.assertTrue(self.T2.is_size_consistent())

        T3 = BinarySearchTreeST()
        self.assertTrue(T3.is_size_consistent())

    def test_is_rank_consistent(self):
        self.assertTrue(self.T1.is_rank_consistent())
        self.assertTrue(self.T2.is_rank_consistent())

        T3 = BinarySearchTreeST()
        self.assertTrue(T3.is_rank_consistent())
