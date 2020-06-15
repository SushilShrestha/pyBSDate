import unittest

from pyBSDate.ADCalendar import ADCalendar


class TestADCalendar(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(ADCalendar(2,1,1).is_leap_year(2300), False)
        self.assertEqual(ADCalendar(2,1,1).is_leap_year(2000), True)
        self.assertEqual(ADCalendar(2,1,1).is_leap_year(2016), True)
        self.assertEqual(ADCalendar(2,1,1).is_leap_year(2015), False)

    def test_month_days_getter(self):
        self.assertEqual(ADCalendar(2016,1,1).get_month_days_in_year(2016),
                         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
        self.assertEqual(ADCalendar(2016,1,1).get_month_days_in_year(2015),
                         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

    def test_count_year_days(self):
        bs_date = ADCalendar(2016, 1, 10)
        count_ = bs_date.count_year_days()
        self.assertEqual(count_, 10)

        count_ = ADCalendar(2016, 3, 13).count_year_days()
        self.assertEqual(count_, 73)

        count_ = ADCalendar(2015, 3, 13).count_year_days()
        self.assertEqual(count_, 72)

        count_ = ADCalendar(2016, 11, 1).count_year_days()
        self.assertEqual(count_, 306)

        count_ = ADCalendar(2015, 8, 16).count_year_days()
        self.assertEqual(count_, 228)


    def test_delta_addition(self):
        self.assertEqual(ADCalendar(2015, 9, 28).add_delta(3).to_string(),
                         "2015-10-01")
        self.assertEqual(ADCalendar(2015, 10, 1).add_delta(31).to_string(),
                         "2015-11-01")
        self.assertEqual(ADCalendar(2015, 11, 16).add_delta(50).to_string(),
                         "2016-01-05")
        self.assertEqual(ADCalendar(2009, 11, 16).add_delta(3703).to_string(),
                         "2020-01-06")

    def test_delta_substraction(self):
        self.assertEqual(ADCalendar(2015,10,2).reduce_delta(2).to_string(),
                         "2015-09-30")
        self.assertEqual(ADCalendar(2015, 11, 1).reduce_delta(31).to_string(),
                         "2015-10-01")
        self.assertEqual(ADCalendar(2073, 1, 5).reduce_delta(50).to_string(),
                         "2072-11-16")
        self.assertEqual(ADCalendar(2020, 1, 6).reduce_delta(3703).to_string(),
                         "2009-11-16")
