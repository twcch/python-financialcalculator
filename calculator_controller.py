from dto.claim_benefit_params import ClaimBenefitParams
from service.impl.discount_calculator_service_impl import DiscountCalculatorServiceImpl


def main():
    discount_calculator()


def discount_calculator():
    claim_benefit_params = ClaimBenefitParams()
    claim_benefit_params.set_payment_amount(40000)
    claim_benefit_params.set_annual_interest_rate_for_discount(0.021)
    claim_benefit_params.set_discount_times(7)

    discount_calculator_service_impl = DiscountCalculatorServiceImpl(claim_benefit_params)
    result = discount_calculator_service_impl.calculate_discount_amount()
    print(result)


if __name__ == '__main__':
    main()
