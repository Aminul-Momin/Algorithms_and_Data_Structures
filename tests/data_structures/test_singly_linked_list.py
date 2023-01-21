import os
import unittest
from ads.fundamentals.singly_linked_list import SLL


class TestSLL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        data = "Algorithms_and_Data_Structures/data/shellsST.txt"
        self.DATA_FILE_PATH = os.path.abspath(os.path.join(os.pardir, data))

        self.SLL2 = SLL()

    @classmethod
    def tearDownClass(self):
        self.SLL2 = None
        self.emptyList = None

    def setUp(self):
        self.SLL1 = SLL()
        self.emptyList = SLL()

    def tearDown(self):
        self.SLL1 = None

    def test_append(self):
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.append(52), None)
        self.assertEqual(self.SLL1.append(51), None)
        self.assertEqual(self.SLL1.append(51), None)
        self.assertEqual(self.SLL1.size(), 3)
        self.assertEqual(self.SLL1.poll(), 52)
        self.assertEqual(self.SLL1.poll(), 51)
        self.assertEqual(self.SLL1.poll(), 51)

    def test_prepend(self):
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.prepend(52), None)
        self.assertEqual(self.SLL1.prepend(51), None)
        self.assertEqual(self.SLL1.prepend(51), None)
        self.assertEqual(self.SLL1.size(), 3)
        self.assertEqual(self.SLL1.poll(), 51)
        self.assertEqual(self.SLL1.poll(), 51)
        self.assertEqual(self.SLL1.poll(), 52)

    def test_insert(self):
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.insert(0, 10), None)
        self.assertEqual(self.SLL1.insert(1, 20), None)
        self.assertEqual(self.SLL1.insert(2, 30), None)
        self.assertEqual(self.SLL1.insert(2, 50), None)
        self.assertEqual(self.SLL1.size(), 4)
        self.assertEqual(self.SLL1.poll(), 10)
        self.assertEqual(self.SLL1.poll(), 20)
        self.assertEqual(self.SLL1.poll(), 50)

        with self.assertRaises(IndexError):
            self.emptyList.insert(1, 100)

    def test_insert_before(self):
        self.assertEqual(self.SLL1._n, 0)
        self.SLL1.insert(0, 20)
        self.assertEqual(self.SLL1.insert_before(20, 30), None)
        self.assertEqual(self.SLL1.insert_before(20, 50), None)
        self.assertEqual(self.SLL1._n, 3)

        with self.assertRaises(RuntimeError):
            self.emptyList.insert_before(0, 100)

    def test_insert_after(self):
        self.assertEqual(self.SLL1._n, 0)
        self.SLL1.insert(0, 20)
        self.assertEqual(self.SLL1.insert_after(20, 30), None)
        self.assertEqual(self.SLL1.insert_after(30, 50), None)
        self.assertEqual(self.SLL1._n, 3)

        with self.assertRaises(RuntimeError):
            self.emptyList.insert_after(None, 100)
            self.emptyList.insert_after(100, None)

    def test_get_first(self):
        self.SLL1.append(30)
        self.SLL1.append(52)
        self.SLL1.append(30)
        self.assertEqual(self.SLL1.size(), 3)
        self.assertEqual(self.SLL1.get_first(), 30)
        self.SLL1.poll()
        self.assertEqual(self.SLL1.get_first(), 52)
        self.SLL1.poll()
        self.assertEqual(self.SLL1.get_first(), 30)

        with self.assertRaises(RuntimeError):
            self.emptyList.get_first()

    def test_get_last(self):
        self.SLL1.append(30)
        self.SLL1.append(52)
        self.SLL1.append(30)
        self.assertEqual(self.SLL1.size(), 3)
        self.assertEqual(self.SLL1.get_last(), 30)
        self.SLL1.remove_last()
        self.assertEqual(self.SLL1.get_last(), 52)
        self.SLL1.remove_last()
        self.assertEqual(self.SLL1.get_last(), 30)

        with self.assertRaises(RuntimeError):
            self.emptyList.get_last()

    def test_get(self):
        self.SLL1.append(30)
        self.SLL1.append(52)
        self.SLL1.append(30)
        self.assertEqual(self.SLL1.size(), 3)
        self.assertEqual(self.SLL1.get(0), 30)
        self.assertEqual(self.SLL1.get(1), 52)
        self.assertEqual(self.SLL1.get(2), 30)

        with self.assertRaises(IndexError):
            self.emptyList.get(1)

    def test_peek(self):
        self.SLL1.append(51)
        self.assertFalse(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.peek(), 51)

        with self.assertRaises(RuntimeError):
            self.emptyList.peek()

    def test_poll(self):
        self.SLL1.append(51)
        self.SLL1.append(52)
        self.SLL1.prepend(52)
        self.assertFalse(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.poll(), 52)
        self.assertEqual(self.SLL1.poll(), 51)
        self.assertEqual(self.SLL1.poll(), 52)

        with self.assertRaises(RuntimeError):
            self.emptyList.poll()

    def test_delete(self):
        self.SLL1.prepend(51)
        self.SLL1.prepend(50)
        self.SLL1.prepend(51)
        self.assertFalse(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.delete(51), None)
        self.assertEqual(self.SLL1.delete(51), None)
        self.assertEqual(self.SLL1.delete(50), None)
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.size(), 0)

        with self.assertRaises(RuntimeError):
            self.SLL1.delete(1)
            self.emptyList.delete(2)
            self.SLL1.peek()

    def test_remove_first(self):
        self.SLL1.prepend(51)
        self.assertFalse(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.remove_first(), None)
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.size(), 0)

        with self.assertRaises(RuntimeError):
            self.SLL1.remove_first()
            self.emptyList.remove_first()
            self.SLL1.peek()

    def test_remove(self):
        self.SLL1.prepend(51)
        self.SLL1.prepend(51)
        self.SLL1.prepend(51)
        self.assertFalse(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.remove(0), None)
        self.assertEqual(self.SLL1.remove(1), None)
        self.assertEqual(self.SLL1.remove(0), None)
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.size(), 0)

        with self.assertRaises(IndexError):
            self.SLL1.remove(1)
            self.emptyList.remove(2)
            self.SLL1.peek()

    def test_remove_last(self):
        self.SLL1.prepend(51)
        self.assertFalse(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.remove_last(), None)
        self.assertTrue(self.SLL1.is_empty())
        self.assertEqual(self.SLL1.size(), 0)

        with self.assertRaises(RuntimeError):
            self.SLL1.remove_last()
            self.emptyList.remove_last()
            self.SLL1.peek()

    def test_index_of(self):
        self.SLL1.append(51)
        self.SLL1.append(52)
        self.SLL1.append(53)
        self.assertAlmostEqual(self.SLL1.index_of(51), 0)
        self.assertAlmostEqual(self.SLL1.index_of(52), 1)
        self.assertAlmostEqual(self.SLL1.index_of(53), 2)
