import unittest
from random import randint
import os

from ads.utils import *
from ads.searching.seperate_chaining_ht import *


class TestSeperateChaininhHashST(unittest.TestCase):
    def setUp(self):
        data = "Algorithms_and_Data_Structures/data/shellsST.txt"
        self.DATA_FILE_PATH = os.path.abspath(os.path.join(os.pardir, data))

        self.numbers = NUMBERS
        self.zip_code = ZIP_CODES

        self.T1 = SeperateChaininhHashST()
        load_data_from_file(self.DATA_FILE_PATH, self.T1)

        self.T2 = SeperateChaininhHashST()
        self.assertTrue(self.T2.is_empty())

    def tearDown(self):
        for key in self.T1.keys():
            self.T1.delete(key)
        assert self.T1.is_empty()
        self.T1 = None

    def test_size(self):
        self.assertEqual(self.T1.size(), 7)
        self.assertNotEqual(self.T1.size(), 0)

        self.T2 = SeperateChaininhHashST()
        self.assertEqual(self.T2.size(), 0)
        load_data_from_collection(self.zip_code, self.T2)
        # for i in self.zip_code.keys(): self.T2.put(i, self.zip_code[i])
        self.assertEqual(self.T2.size(), len(self.T2.keys()))
        self.assertNotEqual(self.T2.size(), 0)

    def test_is_empty(self):
        self.assertFalse(self.T1.is_empty())

        self.T2 = SeperateChaininhHashST()
        self.assertTrue(self.T2.is_empty())
        for i in self.zip_code.keys():
            self.T2.put(i, self.zip_code[i])
        self.assertFalse(self.T2.is_empty())

    def test_get(self):
        self.assertEqual(self.T1.get("by"), 4)
        self.assertEqual(self.T1.get("she"), 0)

        self.assertIsNone(self.T2.get("Lower East Side"))
        self.assertIsNone(self.T2.get(10003))
        for i in self.zip_code.keys():
            self.T2.put(i, self.zip_code[i])

        self.assertEqual(self.T2.get("Lower East Side"), 10003)
        self.assertEqual(self.T2.get(10003), "Lower East Side")
        self.assertEqual(self.T2.get("Lower Manhattan"), 10004)
        self.assertEqual(self.T2.get(10004), "Lower Manhattan")

        with self.assertRaises(ValueError):
            self.T2.get(None)
            self.T1.get(None)

    def test_contains(self):
        self.assertIn("by", self.T1)
        self.assertIn("she", self.T1)
        self.assertNotIn("bye", self.T1)

        self.assertNotIn("Lower East Side", self.T2)
        self.assertNotIn(10003, self.T2)
        for i in self.zip_code.keys():
            self.T2.put(i, self.zip_code[i])

        self.assertIn("Lower East Side", self.T2)
        self.assertIn(10003, self.T2)
        self.assertIn("Lower Manhattan", self.T2)
        self.assertIn(10004, self.T2)

        with self.assertRaises(ValueError):
            self.T2.contains(None)
            self.T1.contains(None)

    def test__resize(self):
        for i in "ABCDEFGH":
            self.i = SeperateChaininhHashST()
            for i in self.zip_code.keys():
                self.i.put(i, self.zip_code[i])
            self.assertEqual(self.i.m, self.i.INIT_CAPACITY)
            self.assertEqual(self.i.n, len(self.zip_code))

        for i in "ABCDEFGH":
            self.i._resize(ord(i))
            self.assertEqual(self.i.m, ord(i))
            self.assertEqual(self.i.n, len(self.zip_code))

    def test_put(self):
        for i in self.zip_code.keys():
            self.T2.put(i, self.zip_code[i])
            self.assertIn(i, self.T2)
        for i in range(100):
            self.T2.put(i, randint(0, 1000))
            self.assertIn(i, self.T2)

        with self.assertRaises(ValueError):
            self.T2.put(None, randint(0, 10))
            self.T1.put(None, randint(0, 10))

        self.T2.put(10003, None)
        self.T2.put("Lower Manhattan", None)

        self.assertNotIn(10003, self.T2)
        self.assertNotIn("Lower Manhattan", self.T2)

    def test_delete(self):
        for i in self.zip_code.keys():
            self.T2.put(i, self.zip_code[i])
            self.assertIn(i, self.T2)
        for i in range(100):
            self.T2.put(i, randint(0, 1000))
            self.assertIn(i, self.T2)

        with self.assertRaises(ValueError):
            self.T2.delete(None)
            self.T1.delete(None)

        self.T2.delete(10004)
        self.T2.delete("Lower East Side")

        self.assertNotIn(10004, self.T2)
        self.assertNotIn("Lower East Side", self.T2)

    def test_keys(self):
        self.assertIn("she", self.T1.keys())
        self.assertIn("sea", self.T1.keys())
        self.assertEqual(len(self.T1.keys()), 7)

        for i in self.zip_code.keys():
            self.T2.put(i, self.zip_code[i])
        self.assertIn(10003, self.T2.keys())
        self.assertIn(10004, self.T2.keys())
        self.assertEqual(len(self.T2.keys()), len(self.zip_code.keys()))
