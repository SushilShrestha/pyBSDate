from pyBSDate.BSCalendar import BSCalendar

__author__ = 'sushil'
import unittest


class TestBSCalendar(unittest.TestCase):
    def test_month_days_getter(self):
        with self.assertRaises(LookupError):
            BSCalendar(2007,2,3).get_month_days_in_year("1968")
            BSCalendar(2045,2,1).get_month_days_in_year("2100")

        self.assertEqual(BSCalendar(2087,1,1).get_month_days_in_year("2087"),
                         [31, 31, 32, 31, 31, 31, 30, 30, 29, 30, 30, 30])

    def test_count_year_days(self):
        bs_date = BSCalendar(2072, 9, 10)
        count_ = bs_date.count_year_days()
        self.assertEqual(count_, 256)

        count_ = BSCalendar(2072, 1, 10).count_year_days()
        self.assertEqual(count_, 10)

        count_ = BSCalendar(2072, 12, 10).count_year_days()
        self.assertEqual(count_, 345)

        print "hello"
        count_ = BSCalendar(2072, 11, 1).count_year_days()
        self.assertEqual(count_, 306)

    def test_delta_addition(self):
        self.assertEqual(BSCalendar(2072,9,30).add_delta(1).to_string(),
                         "2072-10-01")
        self.assertEqual(BSCalendar(2072, 9, 28).add_delta(3).to_string(),
                         "2072-10-01")
        self.assertEqual(BSCalendar(2072, 10, 1).add_delta(29).to_string(),
                         "2072-11-01")
        self.assertEqual(BSCalendar(2072, 11, 16).add_delta(50).to_string(),
                         "2073-01-06")
        self.assertEqual(BSCalendar(2069, 11, 16).add_delta(3703).to_string(),
                         "2080-01-06")

    def test_delta_substraction(self):
        self.assertEqual(BSCalendar(2072,10,1).reduce_delta(1).to_string(),
                         "2072-09-30")
        self.assertEqual(BSCalendar(2072, 10, 1).reduce_delta(3).to_string(),
                         "2072-09-28")
        self.assertEqual(BSCalendar(2072, 11, 1).reduce_delta(29).to_string(),
                         "2072-10-01")
        self.assertEqual(BSCalendar(2073, 1, 6).reduce_delta(50).to_string(),
                         "2072-11-16")
        self.assertEqual(BSCalendar(2080, 1, 6).reduce_delta(3703).to_string(),
                         "2069-11-16")


