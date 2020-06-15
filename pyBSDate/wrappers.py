import datetime

from .utilities import format_functions
from .DateConverter import _bs_to_ad, _ad_to_bs


class bsdate(datetime.date):
    def __new__(cls, year, month, day):
        ad_year, ad_month, ad_day = _bs_to_ad(year, month, day)
        return datetime.date.__new__(cls, ad_year, ad_month, ad_day)

    def __init__(self, year, month, day):
        self.bs_year, self.bs_month, self.bs_day = year, month, day

    @property
    def year(self):
        return self.bs_year

    @property
    def month(self):
        return self.bs_month

    @property
    def day(self):
        return self.bs_day

    @property
    def addate(self):
        ad_year, ad_month, ad_day = _bs_to_ad(self.year, self.month, self.day)
        return addate(ad_year, ad_month, ad_day)

    def strftime(self, fmt, lang='en'):
        for key in format_functions:
            if key in fmt:
                fmt = fmt.replace(key, format_functions[key](self, lang))
        return fmt

    def ctime(self, lang='en'):
        return self.strftime(u"%a %b %d 00:00:00 %Y", lang)

    def isoformat(self, lang='en'):
        return self.strftime(u"%Y-%m-%d", lang)

    def timetuple(self):
        raise NotImplementedError

    def toordinal(self):
        raise NotImplementedError

    def replace(self, year=None, month=None, day=None):
        self.bs_year = year or self.bs_year
        self.bs_month = month or self.bs_month
        self.bs_day = day or self.bs_day

        return bsdate(self.bs_year, self.bs_month, self.bs_day)

    @classmethod
    def today(cls):
        todays_date = datetime.date.today()
        return cls.fromdateobj(todays_date)

    @classmethod
    def fromtimestamp(cls, t):
        timestamp_date = super(bsdate, cls).fromtimestamp(t)
        return cls.fromdateobj(timestamp_date)

    @classmethod
    def fromordinal(cls, n):
        ordinal_date = super(bsdate, cls).fromordinal(n)
        return cls.fromdateobj(ordinal_date)

    @classmethod
    def fromdateobj(cls, d):
        bs_year, bs_month, bs_day = _ad_to_bs(d.year, d.month, d.day)
        return bsdate(bs_year, bs_month, bs_day)


class addate(datetime.date):
    def __init__(self, year, month, day):
        self.bs_year, self.bs_month, self.bs_day = _ad_to_bs(year, month, day)


    @property
    def bsdate(self):
        return bsdate(self.bs_year, self.bs_month, self.bs_day)
