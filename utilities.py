__author__ = 'sushil'
import re
from exceptions import InvalidDateFormat, DateOutOfRange, InvalidDate

import json
DATE_MAP = json.load(open("../datemap.json"))
AD_MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
AD_MONTH_DAYS_LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def validate_date_bs(year, month, day):
    '''
    Answers BS date is valid or not. Raise InvalidDate exception if date is invalid.
    :param year:
    :param month:
    :param day:
    :return: True if valid
    '''
    # We have mapping for the year
    year_calendar = DATE_MAP.get(str(year))
    if not year_calendar:
        raise DateOutOfRange

    if month>12 or day>32:
        raise InvalidDate

    # Month have valid days
    days_in_month = year_calendar['daysonmonth']
    day_in_month = days_in_month[month-1]
    if day>day_in_month:
        raise InvalidDate

    return True

def validate_date_ad(year, month, day):
    '''
    Answers AD date is valid or not. Raise InvalidDate exception if date is invalid.
    :param year:
    :param month:
    :param day:
    :return:
    '''
    # chop off tails we don't want our code to break and too lazy to chop off precise
    validate_date_bs(year+56, 1, 1)
    validate_date_bs(year+57, 1, 1)

    if month>12 or day>31:
        raise InvalidDate

    days_in_month = AD_MONTH_DAYS
    if is_leap_year(year):
        days_in_month = AD_MONTH_DAYS_LEAP
    day_in_month = days_in_month[month-1]
    if day>day_in_month:
        raise InvalidDate

def _bs_to_ad(year, month, day):
    '''
    Convert BS to AD
    :param year: int
    :param month: int
    :param day: int
    :return: AD date for valid BS
    '''
    conversion_information = DATE_MAP.get(str(year))

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
    '''
    Convert AD to BS
    :param year: int
    :param month: int
    :param day: int
    :return: BS date for valid AD
    '''
    # get rough estimates
    bs_year = year + 57
    bs_day = 1
    bs_month = 1

    conversion_information = DATE_MAP.get(str(bs_year))

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

    # if days to add is negative we have to backtrace
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

def _convert_to_days(month, day, days_on_month):
    '''
    Gives number of days from 1st date of the year
    :param month:
    :param day:
    :param days_on_month:
    :return:
    '''
    total_days = 0
    for i in days_on_month[:month-1]:
        total_days += i
    total_days += day-1
    return total_days

def decompose_date(date):
    '''
    Gives tuple of year, month, day if format is valid else raise InvalidFormatException
    :param date:
    :return:
    '''
    re_date_format = r'(\d{4})[\-\/](\d{1,2})[\-\/](\d{1,2})'

    valid_date = re.match(re_date_format, date)
    if not valid_date:
        raise InvalidDateFormat

    year, month, day = map(int, valid_date.groups())

    return year,month,day

def is_leap_year(year):
    '''
    For AD
    :param year:
    :return: boolean
    '''
    if year%4 == 0:
        if year%100 == 0:
            if year%400 ==0:
                return True
            return False
        return True
    return False

