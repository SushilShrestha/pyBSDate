# encoding=utf-8
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


number_map = {
    "0": u"०",
    "1": u"१",
    "2": u"२",
    "3": u"३",
    "4": u"४",
    "5": u"५",
    "6": u"६",
    "7": u"७",
    "8": u"८",
    "9": u"९"
  }


def to_nepali_numbers(number):
    number = str(number)
    return "".join([number_map[i] for i in number])


def weekday_abbr__a(date_obj, lang='en'):
    en = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    np = [u'सोम', u'मंगल', u'बुध', u'बिहि', u'शुक्र', u'शनि', u'आइत']

    if lang == 'en':
        return en[date_obj.weekday()]
    return np[date_obj.weekday()]


def weekday__A(date_obj, lang='en'):
    en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    np = [u'सोमबार', u'मंगलबार', u'बुधबार', u'बिहिबार', u'शुक्रबार', u'शनिबार', u'आइतबार']

    if lang == 'en':
        return en[date_obj.weekday()]
    return np[date_obj.weekday()]


def weekday_as_dec__w(date_obj, lang='en'):
    if lang == 'en':
        return str(date_obj.weekday())
    return to_nepali_numbers(str(date_obj.weekday()))


def day_of_month__d(date_obj, lang='en'):
    en = "%02d" % date_obj.day
    if lang == 'en':
        return en
    return to_nepali_numbers(en)


def month_abbr__b(date_obj, lang='en'):
    en = ['Bai', 'Jes', 'Ashr', 'Shr', 'Bha', 'Asho', 'Kar', 'Man', 'Pou', 'Mag', 'Fal', 'Chai']
    ne = [u'बै', u'जेष्', u'आष', u'श्रा', u'भा', u'असो', u'कार्', u'मं', u'पौ', u'माघ', u'फा', u'चै']
    if lang == 'en':
        return en[date_obj.month - 1]
    return ne[date_obj.month - 1]


def month__B(date_obj, lang='en'):
    en = ['Baisakh', 'Jestha', 'Ashar', 'Shrawan', 'Bhadra', 'Ashoj', 'Kartik', 'Mangsir', 'Poush', 'Magh', 'Falgun', 'Chait']
    ne = [u'बैशाख', u'जेष्ठ', u'आषाढ', u'श्रावन', u'भाद्र', u'असोज', u'कार्तिक', u'मंसिर', u'पौष', u'माघ', u'फागुन', u'चैत्र']
    if lang == 'en':
        return en[date_obj.month - 1]
    return ne[date_obj.month - 1]


def month_as_int__m(date_obj, lang='en'):
    en = '%02d' % date_obj.month
    if lang == 'en':
        return en
    return to_nepali_numbers(en)


def year_without_century__y(date_obj, lang='en'):
    if lang == 'en':
        return str(date_obj.year)[2:]
    return to_nepali_numbers(str(date_obj.year)[2:])


def year__Y(date_obj, lang='en'):
    if lang == 'en':
        return str(date_obj.year)
    return to_nepali_numbers(str(date_obj.year))


def am_pm__p(date_obj, lang='en'):
    return 'AM'


def UTC_offset__z(date_obj, lang='en'):
    raise NotImplementedError


def timezone_name__Z(date_obj, lang='en'):
    raise NotImplementedError


def day_of_the_year__j(date_obj, lang='en'):
    raise NotImplementedError


def week_of_year_sunday__U(date_obj, lang='en'):
    raise NotImplementedError


def week_of_year_sunday__W(date_obj, lang='en'):
    raise NotImplementedError


def locale_appropriate_datetime__c(date_obj, lang='en'):
    raise NotImplementedError


def locale_appropriate_date__x(date_obj, lang='en'):
    raise NotImplementedError


def not_implemented_yet(date_obj, lang='en'):
    raise NotImplementedError


format_functions = {
        '%a': weekday_abbr__a,
        '%A': weekday__A,
        '%w': weekday_as_dec__w,
        '%d': day_of_month__d,
        '%b': month_abbr__b,
        '%B': month__B,
        '%m': month_as_int__m,
        '%y': year_without_century__y,
        '%Y': year__Y,
        '%H': lambda _, __: '00',
        '%I': lambda _, __: '00',
        '%p': am_pm__p,
        '%M': lambda _, __: '00',
        '%S': lambda _, __: '00',
        '%f': lambda _, __: '000000',
        '%z': not_implemented_yet,
        '%Z': not_implemented_yet,
        '%j': not_implemented_yet,
        '%U': not_implemented_yet,
        '%W': not_implemented_yet,
        '%c': not_implemented_yet,
        '%x': not_implemented_yet,
        '%X': lambda _, __: '00:00:00',
        '%%': lambda _, __: '%',
    }