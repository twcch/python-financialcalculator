from service.return_of_premium_calculator_service import ReturnOfPremiumCalculatorService
from service.date_calculator_service import DateCalculatorService
from datetime import datetime

def main():

    p1 = '2022-1-1'
    p2 = '2023-5-1'

    date_calculator_service = DateCalculatorService(p1, p2)
    print(date_calculator_service.calculate_years_difference(0))


if __name__ == '__main__':
    main()