from datetime import datetime
from dto.date_params import DateParams
from service.calculator.impl.date_calculator_service_impl import (
    DateCalculatorServiceImpl,
)


class DateController:
    def __init__(self):
        pass

    def compute_date_difference(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 2)

        date_params = DateParams()
        date_params.set_start_date_for_difference(start_date)
        date_params.set_end_date_for_difference(end_date)
        date_params.set_adjust_months_for_difference(1)

        date_calculator_service_impl = DateCalculatorServiceImpl(date_params)
        result = date_calculator_service_impl.calculate_months_difference()

        print(result)

    def compute_adjust_date(self):
        date = datetime(2023, 1, 1)

        date_params = DateParams()
        date_params.set_date_for_computing(date)
        date_params.set_adjust_days_for_computing(1)

        date_calculator_service_impl = DateCalculatorServiceImpl(date_params)
        result = date_calculator_service_impl.adjust_days_to_date()

        print(result)
