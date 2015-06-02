__author__ = 'sushil'
import unittest

from pyBSDate import BSDate, utilities
from pyBSDate import exceptions


class TestDateConversions_BS2AD(unittest.TestCase):
    def test_wrong_formatting(self):
        wrong_formatted_date = "01-10-2072"
        with self.assertRaises(exceptions.InvalidDateFormat):
            BSDate.convert_to_ad(wrong_formatted_date)

    def test_over_the_range_dates(self):
        over_range_date = "1900-01-10"
        with self.assertRaises(exceptions.DateOutOfRange):
            BSDate.convert_to_ad(over_range_date)

    def test_invalid_month(self):
        invalid_month = "2072-18-10"
        with self.assertRaises(exceptions.InvalidDate):
            BSDate.convert_to_ad(invalid_month)

    def test_invalid_day(self):
        invalid_day = "2072-01-33"
        with self.assertRaises(exceptions.InvalidDate):
            BSDate.convert_to_ad(invalid_day)

    def test_invalid_date(self):
        # no 32 in ashoj 2072
        invalid_date = "2072-06-32"
        with self.assertRaises(exceptions.InvalidDate):
            BSDate.convert_to_ad(invalid_date)

    def test_date_to_days(self):
        year, month, day = 2072, 04, 10
        total_days = 31 + 32 + 31 + 10-1
        days_on_month = [31, 32, 31, 32, 31, 30, 30, 29, 30, 29, 30, 30]
        calc_days = utilities._convert_to_days(4,10, days_on_month)
        self.assertEqual(calc_days, total_days)

    def test_bs_to_ad(self):
        bs_date = "2072-01-10"
        ad_date = "2015-04-23"

        converted_date = BSDate.convert_to_ad(bs_date)
        self.assertEqual(converted_date, ad_date)

    def test_leap_year_test(self):
        bs_date = "2072-11-19"
        ad_date = "2016-03-02"

        converted_date = BSDate.convert_to_ad(bs_date)
        self.assertEqual(converted_date, ad_date)



class TestDateConversions_AD2BS(unittest.TestCase):
    def test_wrong_formatting(self):
        wrong_formatted_date = "01-10-2072"
        with self.assertRaises(exceptions.InvalidDateFormat):
            BSDate.convert_to_bs(wrong_formatted_date)

    def test_over_the_range_dates(self):
        over_range_date = "1913-12-29"
        over_range_date = "2044-01-13"
        with self.assertRaises(exceptions.DateOutOfRange):
            BSDate.convert_to_bs(over_range_date)

    def test_invalid_month(self):
        invalid_month = "2015-18-10"
        with self.assertRaises(exceptions.InvalidDate):
            BSDate.convert_to_bs(invalid_month)

    def test_invalid_day(self):
        invalid_day = "2015-01-33"
        with self.assertRaises(exceptions.InvalidDate):
            BSDate.convert_to_bs(invalid_day)

    def test_invalid_date(self):
        invalid_date = "2016-02-31"
        with self.assertRaises(exceptions.InvalidDate):
            BSDate.convert_to_bs(invalid_date)

    def test_ad_to_bs(self):
        bs_date = "2072-01-10"
        ad_date = "2015-04-23"

        converted_date = BSDate.convert_to_bs(ad_date)
        self.assertEqual(converted_date, bs_date)

        # print _ad_to_bs(2015, 06, 2), "2072-02-19"
        # print _ad_to_bs(2016, 06, 2), "2072-02-20"
        # print _ad_to_bs(2016, 01, 2), "2072-09-18"
        # print _ad_to_bs(2016, 01, 20), "2072-10-06"
