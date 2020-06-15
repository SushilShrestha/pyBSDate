from .DateConverter import _ad_to_bs, _bs_to_ad
from .wrappers import bsdate, addate

def convert_BS_to_AD(year, month, day):
    """
    Converts BS date to AD date
    :param year: year is BS year in int
    :param month: month is BS month in int
    :param day: day is BS Day in int
    :return: (AD year, month, day)
    """
    return _bs_to_ad(year, month, day)


def convert_AD_to_BS(year, month, day):
    """
    Converts AD date to BS date
    :param year: integer AD year
    :param month: integer AD month
    :param day: integer AD day
    :return: (BS year, month, day)
    """
    return _ad_to_bs(year, month, day)

