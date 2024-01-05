from dateutil.relativedelta import relativedelta
from service.calculator.date_calculator_service import DateCalculatorService


class DateCalculatorServiceImpl(DateCalculatorService):
    def __init__(self, date_params):
        self.__date_params = date_params

    def calculate_years_difference(self):
        delta = relativedelta(self.__date_params.get_end_date(), self.__date_params.get_start_date())
        years_difference = delta.years
        result = years_difference + self.__date_params.get_adjust_years()

        return result

    def calculate_months_difference(self):
        delta = relativedelta(self.__date_params.get_end_date(), self.__date_params.get_start_date())
        months_difference = delta.years * 12 + delta.months
        result = months_difference + self.__date_params.get_adjust_months()

        return result

    def calculate_days_difference(self):
        days_difference = self.__date_params.get_end_date() - self.__date_params.get_start_date()
        result = days_difference.days + self.__date_params.get_adjust_days()

        return result
