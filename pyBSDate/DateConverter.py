from .ADCalendar import ADCalendar
from .BSCalendar import BSCalendar

from .DateMap import DATE_MAP

def _bs_to_ad(year, month, day):
    bs_year_data = DATE_MAP.get(str(year))
    if not bs_year_data:
        raise LookupError("BS date out of conversion range")

    anchor_point = bs_year_data["1stbaisakh"]
    anchor_year, anchor_month, anchor_day = anchor_point.split("-")
    anchor_date = ADCalendar(int(anchor_year), int(anchor_month), int(anchor_day))

    bs_date = BSCalendar(year, month, day)
    year_days = bs_date.count_year_days() - 1

    anchor_date.add_delta(year_days)
    return anchor_date.year, anchor_date.month, anchor_date.day

def _ad_to_bs(year, month, day):
    approx_bs_year = year + 57
    bs_year_data = DATE_MAP.get(str(approx_bs_year))
    if not bs_year_data:
        raise LookupError("BS date out of conversion range")

    anchor_point = bs_year_data['1stbaisakh']
    anchor_year, anchor_month, anchor_day = anchor_point.split("-")
    anchor_date = ADCalendar(int(anchor_year), int(anchor_month), int(anchor_day))

    anchor_year_days = anchor_date.count_year_days()

    ad_date = ADCalendar(year, month, day)
    ad_year_days =ad_date.count_year_days()

    days_diff = ad_year_days - anchor_year_days

    bs_date = BSCalendar(approx_bs_year, 1, 1)
    if days_diff>0:
        bs_date.add_delta(days_diff)
    else:
        bs_date.reduce_delta(days_diff*-1)

    return bs_date.year, bs_date.month, bs_date.day
