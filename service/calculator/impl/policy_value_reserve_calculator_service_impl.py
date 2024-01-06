import logging

import decimal
from service.calculator.policy_value_reserve_calculator_service import (
    PolicyValueReserveCalculatorService,
)


class PolicyValueReserveCalculatorServiceImpl(PolicyValueReserveCalculatorService):
    def __init__(self, calim_benfit_params):
        self.__claim_benefit_params = calim_benfit_params

    def calculate_policy_value_reserve_on_base_sum_amount(self):
        logging.info("start: PolicyValueReserveCalculatorServiceImpl.calculate_policy_value_reserve_on_base_sum_amount()")

        result = self.__calculate_policy_value_reserve("B")

        logging.info("end: PolicyValueReserveCalculatorServiceImpl.calculate_policy_value_reserve_on_base_sum_amount()")

        return result

    def calculate_policy_value_reserve_on_paid_up_sum_amount(self):
        logging.info("start: PolicyValueReserveCalculatorServiceImpl.calculate_policy_value_reserve_on_paid_up_sum_amount()")

        result = self.__calculate_policy_value_reserve("P")

        logging.info("end: PolicyValueReserveCalculatorServiceImpl.calculate_policy_value_reserve_on_paid_up_sum_amount()")

        return result

    def calculate_policy_value_reserve_on_total_sum_amount(self):
        logging.info("start: PolicyValueReserveCalculatorServiceImpl.calculate_policy_value_reserve_on_total_sum_amount()")

        result = self.__calculate_policy_value_reserve("T")

        logging.info("end: PolicyValueReserveCalculatorServiceImpl.calculate_policy_value_reserve_on_total_sum_amount()")

        return result

    def __calculate_policy_value_reserve(self, var):
        logging.info("start: PolicyValueReserveCalculatorServiceImpl.__calculate_policy_value_reserve()")

        if var == "B":
            unit_sum_amount = self.__claim_benefit_params.get_unit_base_sum_amount()
        if var == "P":
            unit_sum_amount = self.__claim_benefit_params.get_unit_paid_up_sum_amount()
        if var == "T":
            unit_sum_amount = (
                self.__claim_benefit_params.get_unit_base_sum_amount()
                + self.__claim_benefit_params.get_unit_paid_up_sum_amount()
            )

        result = round(
            decimal.Decimal(
                (
                    (
                        self.__claim_benefit_params.get_ending_policy_value_reserve()
                        - self.__claim_benefit_params.get_beginning_policy_value_reserve()
                    )
                    * self.__claim_benefit_params.get_cumulative_days_for_policy_value_reserve()
                    / self.__claim_benefit_params.get_period_days_for_policy_value_reserve()
                    + self.__claim_benefit_params.get_beginning_policy_value_reserve()
                )
                * unit_sum_amount
            )
        )

        result = round(
            decimal.Decimal(
                result
                * self.__claim_benefit_params.get_multiple_for_policy_value_reserve()
                * self.__claim_benefit_params.get_result_ratio_for_policy_value_reserve()
            ),
            0,
        )

        logging.info("end: PolicyValueReserveCalculatorServiceImpl.__calculate_policy_value_reserve()")

        return result
