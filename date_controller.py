from datetime import datetime
from dto.date_params import DateParams
from service.calculator.impl.date_calculator_service_impl import DateCalculatorServiceImpl


def main():
    compute_date_difference()


def compute_date_difference():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 2)

    date_params = DateParams()
    date_params.set_start_date_for_difference(start_date)
    date_params.set_end_date_for_difference(end_date)
    date_params.set_adjust_months_for_difference(1)

    date_calculator_service_impl = DateCalculatorServiceImpl(date_params)
    result = date_calculator_service_impl.calculate_years_difference()
    print(result)


if __name__ == "__main__":
    main()
