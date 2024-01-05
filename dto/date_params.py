from datetime import datetime


class DateParams():

    def __init__(self):
        # 日期差相關
        self.__start_date_for_difference = datetime(1911, 1, 1)
        self.__end_date_for_difference = datetime(1911, 1, 1)
        self.__adjust_years_for_difference = 0
        self.__adjust_months_for_difference = 0
        self.__adjust_days_for_difference = 0

        # 日期運算相關
        self.__date_for_computing = datetime(1911, 1, 1)
        self.__adjust_years_for_computing = 0
        self.__adjust_months_for_computing = 0
        self.__adjust_days_for_computing = 0

    def get_start_date_for_difference(self):
        return self.__start_date_for_difference

    def set_start_date_for_difference(self, start_date_for_difference):
        self.__start_date_for_difference = start_date_for_difference

    def get_end_date_for_difference(self):
        return self.__end_date_for_difference

    def set_end_date_for_difference(self, end_date_for_difference):
        self.__end_date_for_difference = end_date_for_difference

    def get_adjust_years_for_difference(self):
        return self.__adjust_years_for_difference

    def set_adjust_years_for_difference(self, adjust_years_for_difference):
        self.__adjust_years_for_difference = adjust_years_for_difference

    def get_adjust_months_for_difference(self):
        return self.__adjust_months_for_difference

    def set_adjust_months_for_difference(self, adjust_months_for_difference):
        self.__adjust_months_for_difference = adjust_months_for_difference

    def get_adjust_days_for_difference(self):
        return self.__adjust_days_for_difference

    def set_adjust_days_for_difference(self, adjust_days_for_difference):
        self.__adjust_days_for_difference = adjust_days_for_difference

    def get_date_for_computing(self):
        return self.__date_for_computing

    def set_date_for_computing(self, date_for_computing):
        self.__date_for_computing = date_for_computing

    def get_adjust_years_for_computing(self):
        return self.__adjust_years_for_computing

    def set_adjust_years_for_computing(self, adjust_years_for_computing):
        self.__adjust_years_for_computing = adjust_years_for_computing

    def get_adjust_months_for_computing(self):
        return self.__adjust_months_for_computing

    def set_adjust_months_for_computing(self, adjust_months_for_computing):
        self.__adjust_months_for_computing = adjust_months_for_computing

    def get_adjust_days_for_computing(self):
        return self.__adjust_days_for_computing

    def set_adjust_days_for_computing(self, adjust_days_for_computing):
        self.__adjust_days_for_computing = adjust_days_for_computing