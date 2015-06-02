__author__ = 'sushil'
import unittest
from pyBSDate import utilities
from pyBSDate import exceptions

class TestDateConversions(unittest.TestCase):
    def test_wrong_formatting(self):
        wrong_formatted_date = "01-10-2072"
        with self.assertRaises(exceptions.InvalidDateFormat):
            utilities.convert_to_ad(wrong_formatted_date)

    def test_over_the_range_dates(self):
        over_range_date = "1900-01-10"
        with self.assertRaises(exceptions.DateOutOfRange):
            utilities.convert_to_ad(over_range_date)

    def test_invalid_month(self):
        invalid_month = "2072-18-10"
        with self.assertRaises(exceptions.InvalidDate):
            utilities.convert_to_ad(invalid_month)

    def test_invalid_day(self):
        invalid_day = "2072-01-33"
        with self.assertRaises(exceptions.InvalidDate):
            utilities.convert_to_ad(invalid_day)

    def test_date_to_days(self):
        year, month, day = 2072, 04, 10
        total_days = 31 + 32 + 31 + 10-1
        days_on_month = [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30]
        calc_days = utilities._convert_to_days(4,10, days_on_month)
        self.assertEqual(calc_days, total_days)

    def test_bs_to_ad(self):
        bs_date = "2072-01-10"
        ad_date = "2015-03-23"

        converted_date = utilities.convert_to_ad(bs_date)
        self.assertEqual(converted_date, ad_date)