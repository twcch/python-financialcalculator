from datetime import datetime
from dto.date_params import DateParams
from service.calculator.impl.date_calculator_service_impl import DateCalculatorServiceImpl


def main():
    compute_days_difference()


def compute_days_difference():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 2)

    date_params = DateParams()
    date_params.set_start_date(start_date)
    date_params.set_end_date(end_date)
    date_params.set_adjust_days(1)

    date_calculator_service_impl = DateCalculatorServiceImpl(date_params)
    result = date_calculator_service_impl.calculate_days_difference()
    print(result)


if __name__ == "__main__":
    main()
