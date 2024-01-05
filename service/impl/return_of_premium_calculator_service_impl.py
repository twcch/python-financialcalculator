import decimal
import math
from service.return_of_premium_calculator_service import (
    ReturnOfPremiumCalculatorService,
)


class ReturnOfPremiumCalculatorServiceImpl(ReturnOfPremiumCalculatorService):
    def __init__(self, calim_benfit_params):
        self.__claim_benefit_params = calim_benfit_params

    def calculate_return_of_premium_on_base_sum_amount(self):
        result = self.__calculate_return_of_premium("B")

        return result

    def calculate_return_of_premium_on_paid_up_sum_amount(self):
        result = self.__calculate_return_of_premium("P")

        return result

    def calculate_return_of_premium_on_total_sum_amount(self):
        result = self.__calculate_return_of_premium("T")

        return result

    def __calculate_return_of_premium(self, var):
        unit_premium = round(
            decimal.Decimal(
                self.__claim_benefit_params.get_annualized_standard_unit_premium()
                * self.__claim_benefit_params.get_multiple_for_return_of_premium()
                * min(
                    self.__claim_benefit_params.get_payment_period(),
                    self.__claim_benefit_params.get_insurance_year_at_date_of_loss(),
                )
            ),
            1,
        )

        if var == "B":
            unit_sum_amount = self.__claim_benefit_params.get_unit_base_sum_amount()
        if var == "P":
            unit_sum_amount = self.__claim_benefit_params.get_unit_paid_up_sum_amount()
        if var == "T":
            unit_sum_amount = (
                self.__claim_benefit_params.get_unit_base_sum_amount()
                + self.__claim_benefit_params.get_unit_paid_up_sum_amount()
            )

        if self.__claim_benefit_params.get_currency == "NTD":
            result = round(decimal.Decimal(unit_premium * unit_sum_amount))

        if self.__claim_benefit_params.get_currency == "USD":
            result = math.ceil(decimal.Decimal(unit_premium * unit_sum_amount))

        result = round(
            decimal.Decimal(
                result
                * self.__claim_benefit_params.get_result_ratio_for_return_of_premium()
            )
        )

        return result
