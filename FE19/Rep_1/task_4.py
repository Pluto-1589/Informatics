from task_3 import Backpack, Item
from unittest import TestCase
from task_3 import Backpack
from task_3 import Item


class TestingKit(TestCase):

    # just write one test for the constructor,
    def test_constructor(self):
        expected = 4.0
        actual = Backpack(4.0)

        self.assertEqual(expected, actual)

    # one for each of the three defined methods,
    def test_pack(self):
        expected = Item("water bottle", 0.75)
        actual = Backpack.pack(Item("water bottle", 0.75))

        self.assertEqual(expected, actual)

    def test_unpack(self):
        expected = Item("lighter", 0.05)

        Backpack.pack(Item("lighter", 0.05))
        actual = Backpack.unpack()

        self.assertEqual(expected, actual)

    def test_current_volume(self):
        expected = 0.75
        actual = Backpack.current_volume()

        self.assertEqual(expected, actual)

    # and one that verifies that large items indeed cause an AssertionError.
    def test_(self):

        with self.assertRaises(AssertionError):
            Backpack.pack(Item("camping tent", 20.0))


# GPT's Solution


class TestingKit(TestCase):

    def test_constructor(self):
        backpack = Backpack(4.0)
        expected = 4.0
        self.assertEqual(backpack.max_volume, expected)
        self.assertEqual(backpack.current_volume(), 0)

    def test_pack(self):
        backpack = Backpack(4.0)
        item = Item("water bottle", 0.75)
        backpack.pack(item)
        self.assertIn(item, backpack.packed)
        self.assertEqual(backpack.current_volume(), 0.75)

    def test_unpack(self):
        backpack = Backpack(4.0)
        item1 = Item("lighter", 0.05)
        item2 = Item("water bottle", 0.75)
        backpack.pack(item1)
        backpack.pack(item2)
        unpacked_item = backpack.unpack()
        self.assertEqual(unpacked_item, item2)
        self.assertNotIn(item2, backpack.packed)
        self.assertEqual(backpack.current_volume(), 0.05)

    def test_current_volume(self):
        backpack = Backpack(4.0)
        item = Item("water bottle", 0.75)
        backpack.pack(item)
        self.assertEqual(backpack.current_volume(), 0.75)

    def test_large_item_assertion(self):
        backpack = Backpack(4.0)
        large_item = Item("camping tent", 20.0)
        with self.assertRaises(AssertionError):
            backpack.pack(large_item)
