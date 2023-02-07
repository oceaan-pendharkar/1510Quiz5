from unittest import TestCase
from _sorted import _sorted


class Test(TestCase):
    def test_empty_list(self):
        self.assertEqual(False, _sorted([]))

    def test_single_item(self):
        self.assertTrue(_sorted([566]))

    def test_same_number(self):
        self.assertTrue(_sorted([8, 8, 8, 8]))

    def test_duplicate(self):
        self.assertEqual(True, _sorted([4, 5, 5, 6]))

    def test_negative_sorted(self):
        self.assertEqual(True, _sorted([-9, -8, -7]))

    def test_negative_unsorted(self):
        self.assertFalse(_sorted([-77, -88, -99]))

    def test_positive_sorted(self):
        self.assertEqual(True, _sorted([100, 200, 300]))

    def test_positive_unsorted(self):
        self.assertFalse(_sorted([899, 5, 9]))
