# encoding=utf-8
import datetime
import unittest

from pyBSDate import bsdate, _ad_to_bs, addate


class Test_bsdate(unittest.TestCase):
    def test_month_days_getter(self):
        b = bsdate(2077, 2, 31)
        self.assertEqual(b.year, 2077)
        self.assertEqual(b.month, 2)
        self.assertEqual(b.day, 31)

    def test_ctime(self):
        b = bsdate(2077, 2, 31)
        self.assertEqual(b.ctime(), 'Sat Jes 31 00:00:00 2077')
        self.assertEqual(bsdate(2065, 12, 30).ctime(), 'Sun Chai 30 00:00:00 2065')
        self.assertEqual(bsdate(2065, 12, 30).ctime(lang='ne'), u'आइत चै ३० 00:00:00 २०६५')

    def test_strftime(self):
        b = bsdate(2089, 5, 30)
        self.assertEqual(b.strftime(
            "%a %A %w %d %b %B-%m-%y:%Y %H:%I %p %M:%S.%f %X %%%%"),
            'Thu Thursday 3 30 Bha Bhadra-05-89:2089 00:00 AM 00:00.000000 00:00:00 %%')

    def test_strftime(self):
        b = bsdate(2089, 5, 30)
        self.assertEqual(b.strftime(
            "%a %A %w %d %b %B-%m-%y:%Y %H:%I %p %M:%S.%f %X %%%%", lang='ne'),
            u'बिहि बिहिबार ३ ३० भा भाद्र-०५-८९:२०८९ 00:00 AM 00:00.000000 00:00:00 %%'
        )

    def test_isoformat(self):
        b = bsdate(2098, 8, 1)
        self.assertEqual(b.isoformat(), '2098-08-01')
        self.assertEqual(b.isoformat('ne'), u'२०९८-०८-०१')

    def test_replace(self):
        b = bsdate(2077, 2, 12)
        b = b.replace()
        self.assertEqual(b.ctime(), 'Mon Jes 12 00:00:00 2077')
        b = b.replace(year=2079)
        self.assertEqual(b.ctime(), bsdate(2079, 2, 12).ctime())

    def test_less_than_equals(self):
        b = bsdate(2077, 2, 12) # 2020-05-25
        self.assertEqual(b < datetime.date(2020, 5, 25), False)
        self.assertEqual(b <= datetime.date(2020, 5, 25), True)

        c = bsdate(2077, 1, 1)
        self.assertEqual(c < b, True)
        self.assertEqual(c <= b, True)

    def test_greater_than_equals(self):
        b = bsdate(2077, 2, 12)  # 2020-05-25
        self.assertEqual(b > datetime.date(2020, 5, 25), False)
        self.assertEqual(b >= datetime.date(2020, 5, 25), True)
        self.assertEqual(b > datetime.date(2019, 5, 25), True)

    def test_today(self):
        b = bsdate.today()
        a = datetime.date.today()
        bs_year, bs_month, bs_day = _ad_to_bs(a.year, a.month, a.day)
        self.assertEqual(b, bsdate(bs_year, bs_month, bs_day))

    def test_timestamp(self):
        b = bsdate.fromtimestamp(1592097802)
        self.assertEqual(b, bsdate(2077, 2, 31))

    def test_fromdateobj(self):
        test = datetime.date(2012, 2, 29)
        b = bsdate.fromdateobj(test)
        self.assertEqual(b, bsdate(2068, 11, 17))

    def test_addate(self):
        b = bsdate(2077, 2, 15)  # 2020-05-28
        a = b.addate
        c = a.bsdate
        self.assertEqual(b, c)
        self.assertEqual(a, datetime.date(2020, 5, 28))


class Test_addate(unittest.TestCase):
    def test_addate(self):
        a = addate(2020, 6, 14)
        self.assertEqual(a.ctime(), 'Sun Jun 14 00:00:00 2020')

    def test_convert(self):
        a = addate(2020, 6, 14)
        b = a.bsdate
        self.assertEqual(b.ctime(), 'Sun Jes 32 00:00:00 2077')
        self.assertEqual(b.ctime('ne'), u'आइत जेष् ३२ 00:00:00 २०७७')

    def test_001(self):
        ne_date = bsdate(2077, 2, 32)
        # self.assertEqual(ne_date.strftime("%B %d %Y, %A", lang='ne'), '')
        en_date = ne_date.addate
        print(en_date.strftime("%B %d %Y, %A"))
        self.assertEqual(en_date.strftime("%B %d %Y, %A"), 'June 14 2020, Sunday')
