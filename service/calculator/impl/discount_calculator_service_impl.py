import decimal
from service.calculator.discount_calculator_service import DiscountCalculatorService


class DiscountCalculatorServiceImpl(DiscountCalculatorService):
    def __init__(self, claim_benefit_params):
        self.__claim_benefit_params = claim_benefit_params

    def calculate_monthly_interest_rate_for_discount(self):
        annual_interest_rate_for_discount = (
            self.__claim_benefit_params.get_annual_interest_rate_for_discount()
        )
        monthly_interest_rate_for_discount = round(
            decimal.Decimal((1 + annual_interest_rate_for_discount) ** (1 / 12) - 1), 9
        )

        return monthly_interest_rate_for_discount

    def calculate_monthly_discount_rate(self):
        annual_interest_rate_for_discount = (
            self.__claim_benefit_params.get_annual_interest_rate_for_discount()
        )
        monthly_discount_rate = round(
            decimal.Decimal((1 + annual_interest_rate_for_discount) ** (-1 / 12)), 9
        )

        return monthly_discount_rate

    def calculate_discount_amount(self):
        payment_amount = self.__claim_benefit_params.get_payment_amount()
        times = self.__claim_benefit_params.get_discount_times()
        monthly_interest_rate_for_discount = (
            self.calculate_monthly_interest_rate_for_discount()
        )
        monthly_discount_rate = self.calculate_monthly_discount_rate()

        discount_amount = round(
            decimal.Decimal(
                payment_amount
                * (1 - monthly_discount_rate**times)
                / (monthly_interest_rate_for_discount * monthly_discount_rate)
            ),
            0,
        )

        return discount_amount
