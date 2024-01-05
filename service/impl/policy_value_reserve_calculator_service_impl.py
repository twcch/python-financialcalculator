import decimal
from service.policy_value_reserve_calculator_service import (
    PolicyValueReserveCalculatorService,
)


class PolicyValueReserveCalculatorServiceImpl(PolicyValueReserveCalculatorService):
    def __init__(self, calim_benfit_params):
        self.__claim_benefit_params = calim_benfit_params

    def calculate_policy_value_reserve_on_base_sum_amount(self):
        result = self.__calculate_policy_value_reserve("B")

        return result

    def calculate_policy_value_reserve_on_paid_up_sum_amount(self):
        result = self.__calculate_policy_value_reserve("P")

        return result

    def calculate_policy_value_reserve_on_total_sum_amount(self):
        result = self.__calculate_policy_value_reserve("T")

        return result

    def __calculate_policy_value_reserve(self, var):
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

        return result
