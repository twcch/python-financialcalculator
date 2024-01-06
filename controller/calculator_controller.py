from dto.claim_benefit_params import ClaimBenefitParams
from service.calculator.impl.discount_calculator_service_impl import (
    DiscountCalculatorServiceImpl,
)

import logging


class CalculatorController:
    def __init__(self):
        pass

    def compute_discount(self):
        claim_benefit_params = ClaimBenefitParams()
        claim_benefit_params.set_payment_amount(40000)
        claim_benefit_params.set_annual_interest_rate_for_discount(0.021)
        claim_benefit_params.set_discount_times(7)

        discount_calculator_service_impl = DiscountCalculatorServiceImpl(
            claim_benefit_params
        )

        result = discount_calculator_service_impl.calculate_discount_amount()

        return result
