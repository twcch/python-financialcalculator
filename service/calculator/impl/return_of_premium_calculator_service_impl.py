import logging

import decimal
import math
from service.calculator.return_of_premium_calculator_service import (
    ReturnOfPremiumCalculatorService,
)


class ReturnOfPremiumCalculatorServiceImpl(ReturnOfPremiumCalculatorService):
    def __init__(self, calim_benfit_params):
        self.__claim_benefit_params = calim_benfit_params

    def calculate_return_of_premium_on_base_sum_amount(self):
        logging.info("start: ReturnOfPremiumCalculatorServiceImpl.calculate_return_of_premium_on_base_sum_amount()")

        result = self.__calculate_return_of_premium("B")

        logging.info("end: ReturnOfPremiumCalculatorServiceImpl.calculate_return_of_premium_on_base_sum_amount()")

        return result

    def calculate_return_of_premium_on_paid_up_sum_amount(self):
        logging.info("start: ReturnOfPremiumCalculatorServiceImpl.calculate_return_of_premium_on_paid_up_sum_amount()")

        result = self.__calculate_return_of_premium("P")

        logging.info("end: ReturnOfPremiumCalculatorServiceImpl.calculate_return_of_premium_on_paid_up_sum_amount()")

        return result

    def calculate_return_of_premium_on_total_sum_amount(self):
        logging.info("start: ReturnOfPremiumCalculatorServiceImpl.calculate_return_of_premium_on_total_sum_amount()")

        result = self.__calculate_return_of_premium("T")

        logging.info("end: ReturnOfPremiumCalculatorServiceImpl.calculate_return_of_premium_on_total_sum_amount()")

        return result

    def __calculate_return_of_premium(self, var):
        logging.info("start: ReturnOfPremiumCalculatorServiceImpl.__calculate_return_of_premium()")

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

        if self.__claim_benefit_params.get_currency() == "NTD":
            result = round(decimal.Decimal(unit_premium * unit_sum_amount))

        if self.__claim_benefit_params.get_currency() == "USD":
            result = math.ceil(decimal.Decimal(unit_premium * unit_sum_amount))

        result = round(
            decimal.Decimal(
                result
                * self.__claim_benefit_params.get_result_ratio_for_return_of_premium()
            )
        )

        logging.info("end: ReturnOfPremiumCalculatorServiceImpl.__calculate_return_of_premium()")

        return result
