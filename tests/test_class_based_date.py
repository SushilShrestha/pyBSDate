from pyBSDate import bsdate

__author__ = 'sushil'
import unittest


class Test_bsdate(unittest.TestCase):
    def test_month_days_getter(self):
        b = bsdate(2077, 2, 31)
        self.assertEqual(b.year, 2077)
        self.assertEqual(b.month, 2)
        self.assertEqual(b.day, 31)


