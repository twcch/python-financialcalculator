from dto.claim_benefit_params import ClaimBenefitParams
from service.calculator.impl.discount_calculator_service_impl import (
    DiscountCalculatorServiceImpl,
)


class CalculatorController:
    def __init__(self):
        self.__claim_benefit_params = ClaimBenefitParams()
        self.__claim_benefit_params.set_payment_amount(40000)
        self.__claim_benefit_params.set_annual_interest_rate_for_discount(0.021)
        self.__claim_benefit_params.set_discount_times(7)



    def compute_discount(self):
        discount_calculator_service_impl = DiscountCalculatorServiceImpl(
            self.__claim_benefit_params
        )

        result = discount_calculator_service_impl.calculate_discount_amount()

        return result
