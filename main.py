from dto.benefit_params import BenefitParams
from service.discount_calculator_service import DiscountCalculatorService

def main():
    benefit_params = BenefitParams()
    benefit_params.set_payment_amount(10000)
    benefit_params.set_annual_discount_rate(0.01)
    benefit_params.set_discount_times(1)
    
    discount_calculator_service = DiscountCalculatorService(benefit_params)
    result = discount_calculator_service.calculate_monthly_discount_rate()
    print(result)

if __name__ == '__main__':
    main()