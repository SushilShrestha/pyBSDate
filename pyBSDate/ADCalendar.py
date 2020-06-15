from .BaseCalendar import BaseCalendar

class ADCalendar(BaseCalendar):
    def __init__(self, year_, month_, day_):
        super(ADCalendar, self).__init__(year_, month_, day_)

    def get_month_days_in_year(self, year):
        if self.is_leap_year(year):
            return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    return True
                return False
            return True
        return False
