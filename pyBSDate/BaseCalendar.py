import operator
from functools import reduce


class BaseCalendar(object):
    """
    Base templates for bscalendar and ad calendar.
    Will be able to do things like add delta, reduce delta.
    """
    year,month,day = None,None,None
    def __init__(self, year_, month_, day_):
        try:
            self.year = int(year_)
            self.month = int(month_)
            self.day = int(day_)
        except ValueError:
            raise ValueError("Invalid Date")

        self.validate_date()

    def add_delta(self, numDays):
        days_in_month = self.get_days_in_month(self.year, self.month)
        days_left_in_month = days_in_month - self.day

        if (numDays < days_left_in_month):
            self.day += numDays
            return self

        numDays -= days_left_in_month
        if numDays == 0:
            self.day = days_in_month
            return self

        self.day = 0
        self.month += 1
        if (self.month > 12):
            self.month = self.month%12
            self.year += 1

        return self.add_delta(numDays)

    def reduce_delta(self, numDays):
        days_left_in_month = self.day

        if numDays < days_left_in_month:
            self.day -= numDays
            return self

        self.month -= 1
        if self.month < 1:
            self.month = 12
            self.year -= 1
        days_in_month = self.get_days_in_month(self.year, self.month)
        self.day = days_in_month

        numDays -= days_left_in_month
        return self.reduce_delta(numDays)

    def count_year_days(self):
        days_in_year = self.get_month_days_in_year(self.year)
        days_list = days_in_year[:self.month-1]

        days_count = 0
        if days_list:
            days_count = reduce(operator.add, days_in_year[:self.month-1])

        days_count += self.day
        return days_count

    def get_days_in_month(self, year, month):
        days_in_year = self.get_month_days_in_year(year)
        days_in_month = days_in_year[month-1]
        return days_in_month

    def get_month_days_in_year(self, year):
        raise NotImplementedError

    def validate_date(self):
        if self.month>12 or self.month<1:
            raise ValueError("Invalid Date")
        if self.day<1:
            raise ValueError("Invalid Date")

        days_in_month = self.get_days_in_month(self.year, self.month)
        if self.day>days_in_month:
            raise ValueError("Invalid Date")

    def get_previous_month_days(self, year, month):
        month -= 1
        if month <=0:
            year -= 1
            month = 12
        return self.get_days_in_month(year, month)

    def to_string(self):
        return "%04d-%02d-%02d" %(self.year, self.month, self.day)