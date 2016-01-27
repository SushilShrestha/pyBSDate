__author__ = 'sushil'
import re


def decompose_date(date):
    '''
    Gives tuple of year, month, day if format is valid else raise InvalidFormatException
    :param date:
    :return:
    '''
    re_date_format = r'(\d{4})[\-\/](\d{1,2})[\-\/](\d{1,2})'

    valid_date = re.match(re_date_format, date)
    if not valid_date:
        raise ValueError("Invalid date format! Date should be of format yyyy-mm-dd")

    year, month, day = map(int, valid_date.groups())

    return year,month,day
