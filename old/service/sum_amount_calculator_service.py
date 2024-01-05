import decimal


class ReturnOfPremiumCalculatorService:

    def __init__(self):
        self.__vpu = 10000
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__multiple = 1
        self.__result_ratio = 1

    def calculate_sum_amount_on_base_sum_amount(self):
        result = self.__calculate_sum_amount('B')

        return result

    def calculate_sum_amount_on_paid_up_sum_amount(self):
        result = self.__calculate_sum_amount('P')

        return result

    def calculate_sum_amount_on_total_sum_amount(self):
        result = self.__calculate_sum_amount('T')

        return result

    def __calculate_sum_amount(self, var):
        if (var == 'B'):
            unit_sum_amount = self.__unit_base_sum_amount

        if (var == 'P'):
            unit_sum_amount = self.__unit_paid_up_sum_amount

        if (var == 'T'):
            unit_sum_amount = self.__unit_base_sum_amount + self.__unit_paid_up_sum_amount

        result = round(decimal.Decimal(unit_sum_amount * self.__vpu * self.__multiple * self.__result_ratio))

        return result

    def get_vpu(self):
        return self.__vpu

    def set_vpu(self, vpu):
        self.__vpu = vpu

    def get_unit_base_sum_amount(self):
        return self.__unit_base_sum_amount

    def set_unit_base_sum_amount(self, unit_base_sum_amount):
        self.__unit_base_sum_amount = unit_base_sum_amount

    def get_unit_paid_up_sum_amount(self):
        return self.__unit_paid_up_sum_amount

    def set_uunit_paid_up_sum_amount(self, unit_paid_up_sum_amount):
        self.__unit_paid_up_sum_amount = unit_paid_up_sum_amount

    def get_multiple(self):
        return self.__multiple

    def set_multiple(self, multiple):
        self.__multiple = multiple

    def get_result_ratio(self):
        return self.__result_ratio

    def set_result_ratio(self, result_ratio):
        self.__result_ratio = result_ratio
