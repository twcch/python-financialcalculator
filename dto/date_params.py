from datetime import datetime


class DateParams():

    def __init__(self):
        self.__start_date = datetime(1911, 1, 1)
        self.__end_date = datetime(1911, 1, 1)
        self.__adjust_years = 0
        self.__adjust_months = 0
        self.__adjust_days = 0

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def get_adjust_years(self):
        return self.__adjust_years

    def set_adjust_years(self, adjust_years):
        self.__adjust_years = adjust_years

    def get_adjust_months(self):
        return self.__adjust_months

    def set_adjust_months(self, adjust_months):
        self.__adjust_months = adjust_months

    def get_adjust_days(self):
        return self.__adjust_days

    def set_adjust_days(self, adjust_days):
        self.__adjust_days = adjust_days
