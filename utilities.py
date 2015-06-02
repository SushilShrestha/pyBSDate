__author__ = 'sushil'
import re
from exceptions import InvalidDateFormat, DateOutOfRange, InvalidDate
def convert_to_ad(bs_date):
    well_behaved_date = decompose_date(bs_date)
    year, month, day = well_behaved_date

    ad_year, ad_month, ad_day = _bs_to_ad(year, month, day)
    formatted_date = "{}-{:02}-{:02}".format(ad_year, ad_month, ad_day)
    return formatted_date

def convert_to_bs(ad_date):
    well_behaved_date = decompose_date(ad_date)
    year, month, day = well_behaved_date

    bs_year, bs_month, bs_day = _ad_to_bs(year, month, day)
    formatted_date = "{}-{:02}-{:02}".format(bs_year, bs_month, bs_day)
    return formatted_date

import json
DATE_MAP = json.load(open("../datemap.json"))
AD_MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
AD_MONTH_DAYS_LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def _bs_to_ad(year, month, day):
    conversion_information = DATE_MAP.get(str(year))
    if not conversion_information:
        raise DateOutOfRange

    first_day_on_year = conversion_information['1stbaisakh']
    ad_year, ad_month, ad_day = decompose_date(first_day_on_year)

    month_days_on_year = conversion_information['daysonmonth']
    total_num_days = _convert_to_days(month, day, month_days_on_year)

    ad_day += total_num_days
    days_in_month = AD_MONTH_DAYS
    day_in_month = days_in_month[ad_month-1]
    while(ad_day > day_in_month):
        ad_day -= day_in_month
        ad_month += 1
        if ad_month>12:
            ad_month = 1
            ad_year += 1
            if is_leap_year(ad_year):
                # leap_year data is not important in outer because feb is behind april
                days_in_month = AD_MONTH_DAYS_LEAP

        day_in_month = days_in_month[ad_month-1]
    return ad_year, ad_month, ad_day

def _ad_to_bs(year, month, day):
    bs_year = year + 57
    bs_day = 1
    bs_month = 1

    conversion_information = DATE_MAP.get(str(bs_year))
    if not conversion_information:
        raise DateOutOfRange

    first_day_on_year = conversion_information['1stbaisakh']
    ad_year, ad_month, ad_day = decompose_date(first_day_on_year)

    days_in_month = conversion_information['daysonmonth']

    ad_month_days = AD_MONTH_DAYS
    if is_leap_year(year):
        ad_month_days = AD_MONTH_DAYS_LEAP

    total_num_days_to_add = _convert_to_days(month, day, ad_month_days)
    total_num_days_to_add -= _convert_to_days(ad_month, ad_day, ad_month_days)

    if total_num_days_to_add>0:
        # forward from april==>
        bs_day += total_num_days_to_add
        day_in_month = days_in_month[bs_month-1]
        while(bs_day>day_in_month):
            bs_day -=day_in_month
            bs_month += 1
            if bs_month>12:
                bs_month = 1
                bs_year += 1
            day_in_month = days_in_month[bs_month-1]
        return bs_year, bs_month, bs_day

    # backward from <==april
    bs_day += total_num_days_to_add

    conversion_information = DATE_MAP.get(str(bs_year-1))
    days_in_month = conversion_information['daysonmonth']
    while (bs_day<0):
        bs_month -= 1
        if bs_month<1:
            bs_month = 12
            bs_year -= 1
        days_in_previous_month = days_in_month[bs_month-1]
        bs_day += days_in_previous_month
    return bs_year, bs_month, bs_day

    pass

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

    if month<1 or month>12:
        raise InvalidDate

    if day<1 or day>32:
        raise InvalidDate

    return year,month,day

def is_leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 ==0:
                return True
            return False
        return True
    return False

