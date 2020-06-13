__author__ = 'sushil'

import datetime
from .utilities import decompose_date, format_functions
from .DateConverter import _bs_to_ad, _ad_to_bs


def convert_to_ad(bs_date):
    date_components = decompose_date(bs_date)
    year, month, day = date_components

    ad_year, ad_month, ad_day = _bs_to_ad(year, month, day)
    formatted_date = "{}-{:02}-{:02}".format(ad_year, ad_month, ad_day)
    return formatted_date


def convert_to_bs(ad_date):
    date_components = decompose_date(ad_date)
    year, month, day = date_components

    bs_year, bs_month, bs_day = _ad_to_bs(year, month, day)
    formatted_date = "{}-{:02}-{:02}".format(bs_year, bs_month, bs_day)
    return formatted_date


class nepalidate(datetime.date):
    def __init__(self, year, month, day):
        super(nepalidate, self).__init__(year, month, day)


class bsdate(nepalidate):
    def __new__(cls, year, month, day):
        ad_year, ad_month, ad_day = _bs_to_ad(year, month, day)
        return nepalidate.__new__(cls, ad_year, ad_month, ad_day)

    def __init__(self, year, month, day):
        self.bs_year, self.bs_month, self.bs_day = year, month, day
        super(bsdate, self).__init__(self.year, self.month, self.day)

    @property
    def year(self):
        return self.bs_year

    @property
    def month(self):
        return self.bs_month

    @property
    def day(self):
        return self.bs_day

    def strftime(self, fmt, lang='en'):
        for key in format_functions:
            if key in fmt:
                fmt = fmt.replace(key, format_functions[key](self, lang))
        return fmt
    
    def ctime(self):
        return self.strftime("%a %b %d 00:00:00 %Y")
