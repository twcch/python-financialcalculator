from datetime import datetime

from service.date_difference_calculator_service import DateDifferenceCalculatorService


class DateCalculatorService:
    def __init__(self, str_start_date, str_end_date):
        self.__start_date = datetime.strptime(str_start_date, "%Y-%m-%d")
        self.__end_date = datetime.strptime(str_end_date, "%Y-%m-%d")
        self.__date_difference_calculator_service = DateDifferenceCalculatorService(
            str_start_date, str_end_date
        )

    def calculate_start_date_for_policy_value_reserve(self):
        pass

    def calculate_period_days_for_policy_value_reserve(self):
        pass

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date
