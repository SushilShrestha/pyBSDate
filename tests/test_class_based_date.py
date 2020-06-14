# encoding=utf-8
from pyBSDate import bsdate

__author__ = 'sushil'
import unittest


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
        b.replace()
        self.assertEqual(b.ctime(), 'Mon Jes 12 00:00:00 2077')
        b = b.replace(year=2079)
        self.assertEqual(b.ctime(), bsdate(2079, 2, 12).ctime())

