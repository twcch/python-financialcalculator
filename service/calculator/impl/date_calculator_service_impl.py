from service.calculator.date_calculator_service import DateCalculatorService


class DateCalculatorServiceImpl(DateCalculatorService):
    def __init__(self, date_params):
        self.__date_params = date_params

    def calculate_days_difference(self):
        days_difference = self.__date_params.get_end_date() - self.__date_params.get_start_date()
        result = days_difference.days + self.__date_params.get_adjust_days()

        return result