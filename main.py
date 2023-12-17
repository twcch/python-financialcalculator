from service.return_of_premium_calculator import ReturnOfPremiumCalculator

def main():
    return_of_premium_calculator = ReturnOfPremiumCalculator()

    return_of_premium_calculator.set_annualized_standard_unit_premium(20)

    print(return_of_premium_calculator.get_annualized_standard_unit_premium())


if __name__ == '__main__':
    main()