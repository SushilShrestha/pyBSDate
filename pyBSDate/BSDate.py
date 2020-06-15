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
