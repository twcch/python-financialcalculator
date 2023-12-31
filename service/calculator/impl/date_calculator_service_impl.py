import logging

from service.calculator.date_calculator_service import DateCalculatorService
from dateutil.relativedelta import relativedelta


class DateCalculatorServiceImpl(DateCalculatorService):
    def __init__(self, date_params):
        self.__date_params = date_params

    def calculate_years_difference(self):
        logging.info("start: DateCalculatorServiceImpl.calculate_years_difference()")

        delta = relativedelta(
            self.__date_params.get_end_date_for_difference(),
            self.__date_params.get_start_date_for_difference(),
        )
        years_difference = delta.years
        result = years_difference + self.__date_params.get_adjust_years_for_difference()

        logging.info("end: DateCalculatorServiceImpl.calculate_years_difference()")

        return result

    def calculate_months_difference(self):
        logging.info("start: DateCalculatorServiceImpl.calculate_months_difference()")

        delta = relativedelta(
            self.__date_params.get_end_date_for_difference(),
            self.__date_params.get_start_date_for_difference(),
        )
        months_difference = delta.years * 12 + delta.months
        result = (
                months_difference + self.__date_params.get_adjust_months_for_difference()
        )

        logging.info("end: DateCalculatorServiceImpl.calculate_months_difference()")

        return result

    def calculate_days_difference(self):
        logging.info("start: DateCalculatorServiceImpl.calculate_days_difference()")

        days_difference = (
                self.__date_params.get_end_date_for_difference()
                - self.__date_params.get_start_date_for_difference()
        )
        result = (
                days_difference.days + self.__date_params.get_adjust_days_for_difference()
        )

        logging.info("end: DateCalculatorServiceImpl.calculate_days_difference()")

        return result

    def adjust_years_to_date(self):
        logging.info("start: DateCalculatorServiceImpl.adjust_years_to_date()")

        result = self.__date_params.get_date_for_computing() + relativedelta(
            years=self.__date_params.get_adjust_years_for_computing()
        )

        result = result.strftime("%Y-%m-%d")

        logging.info("end: DateCalculatorServiceImpl.adjust_years_to_date()")

        return result

    def adjust_months_to_date(self):
        logging.info("start: DateCalculatorServiceImpl.adjust_months_to_date()")

        result = self.__date_params.get_date_for_computing() + relativedelta(
            months=self.__date_params.get_adjust_months_for_computing()
        )

        result = result.strftime("%Y-%m-%d")

        logging.info("end: DateCalculatorServiceImpl.adjust_months_to_date()")

        return result

    def adjust_days_to_date(self):
        logging.info("start: DateCalculatorServiceImpl.adjust_days_to_date()")

        result = self.__date_params.get_date_for_computing() + relativedelta(
            days=self.__date_params.get_adjust_days_for_computing()
        )

        result = result.strftime("%Y-%m-%d")

        logging.info("end: DateCalculatorServiceImpl.adjust_days_to_date()")

        return result
