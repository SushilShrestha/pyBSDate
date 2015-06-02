__author__ = 'sushil'
import re
from exceptions import InvalidDateFormat, DateOutOfRange, InvalidDate
def convert_to_ad(bs_date):
    well_behaved_date = decompose_date(bs_date)
    year, month, day = well_behaved_date

    ad_year, ad_month, ad_day = _ad_to_bs(year, month, day)
    return "{}-{:02}-{:02}".format(ad_year, ad_month, ad_day)
    pass

import json
DATE_MAP = json.load(open("../datemap.json"))
AD_MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def _ad_to_bs(year, month, day):
    conversion_information = DATE_MAP.get(str(year))

    first_day_on_year = conversion_information['1stbaisakh']
    ad_year, ad_month, ad_day = decompose_date(first_day_on_year)

    month_days_on_year = conversion_information['daysonmonth']
    total_num_days = _convert_to_days(month, day, month_days_on_year)

    ad_day += total_num_days
    day_in_month = AD_MONTH_DAYS[ad_month-1]
    while(ad_day > day_in_month):
        ad_day -= day_in_month
        ad_month += 1
        if ad_month>12:
            ad_month = 1
            ad_year += 1

        day_in_month = AD_MONTH_DAYS[ad_month-1]
    return ad_year, ad_month, ad_day







def _convert_to_days(month, day, days_on_month):
    total_days = 0
    for i in days_on_month[:month-1]:
        total_days += i
    total_days += day-1
    return total_days

def decompose_date(date):
    re_date_format = r'(\d{4})[\-\/](\d{1,2})[\-\/](\d{1,2})'

    valid_date = re.match(re_date_format, date)
    if not valid_date:
        raise InvalidDateFormat

    year, month, day = valid_date.groups()

    year = int(year)
    month = int(month)
    day = int(day)

    if year<1970 or year>2100:
        raise DateOutOfRange

    if month<1 or month>12:
        raise InvalidDate

    if day<1 or day>32:
        raise InvalidDate

    return year,month,day
