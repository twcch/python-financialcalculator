import decimal
from service.return_of_premium_calculator_service import ReturnOfPremiumCalculatorService


class ReturnOfPremiumCalculatorServiceImpl(ReturnOfPremiumCalculatorService):
    def __init__(self, calim_benfit_params):
        self.__claim_benefit_params = calim_benfit_params

    def calculate_return_of_premium_on_base_sum_amount(self):
        result = self.__calculate_sum_amount('B')

        return result

    def calculate_return_of_premium_on_paid_up_sum_amount(self):
        result = self.__calculate_sum_amount('P')

        return result

    def calculate_return_of_premium_on_total_sum_amount(self):
        result = self.__calculate_sum_amount('T')

        return result

    def __calculate_return_of_premium(self, var):
        if var == 'B':
            unit_sum_amount = self.__claim_benefit_params.get_unit_base_sum_amount()
        if var == 'P':
            unit_sum_amount = self.__claim_benefit_params.get_unit_paid_up_sum_amount()
        if var == 'T':
            unit_sum_amount = (
                self.__claim_benefit_params.get_unit_base_sum_amount()
                + self.__claim_benefit_params.get_unit_paid_up_sum_amount()
            )

        return unit_sum_amount
