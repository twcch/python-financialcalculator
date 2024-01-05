import decimal
from service.calculator.sum_amount_calculator_service import SumAmountCalculatorService


class SumAmountCalculatorServiceImpl(SumAmountCalculatorService):
    def __init__(self, calim_benfit_params):
        self.__claim_benefit_params = calim_benfit_params

    def calculate_sum_amount_on_base_sum_amount(self):
        result = self.__calculate_sum_amount("B")

        return result

    def calculate_sum_amount_on_paid_up_sum_amount(self):
        result = self.__calculate_sum_amount("P")

        return result

    def calculate_sum_amount_on_total_sum_amount(self):
        result = self.__calculate_sum_amount("T")

        return result

    def __calculate_sum_amount(self, var):
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
                unit_sum_amount
                * self.__claim_benefit_params.get_vpu()
                * self.__claim_benefit_params.get_multiple_for_sum_amount()
                * self.__claim_benefit_params.get_result_ratio_for_sum_amount()
            ),
            0,
        )

        return result
