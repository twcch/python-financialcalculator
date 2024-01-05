class ClaimBenefitParams:
    def __init__(self):
        # 保額相關
        self.__vpu = 10000
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__multiple_for_sum_amount = 1
        self.__result_ratio_for_sum_amount = 1

        # 貼現相關
        self.__payment_amount = 0
        self.__annual_interest_rate_for_discount = 0
        self.__discount_times = 0

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

    def set_unit_paid_up_sum_amount(self, unit_paid_up_sum_amount):
        self.__unit_paid_up_sum_amount = unit_paid_up_sum_amount

    def get_multiple_for_sum_amount(self):
        return self.__multiple_for_sum_amount

    def set_multiple_for_sum_amount(self, multiple_for_sum_amount):
        self.__multiple_for_sum_amount = multiple_for_sum_amount

    def get_result_ratio_for_sum_amount(self):
        return self.__result_ratio_for_sum_amount

    def set_result_ratio_for_sum_amount(self, result_ratio_for_sum_amount):
        self.__result_ratio_for_sum_amount = result_ratio_for_sum_amount

    def get_payment_amount(self):
        return self.__payment_amount

    def set_payment_amount(self, payment_amount):
        self.__payment_amount = payment_amount

    def get_annual_interest_rate_for_discount(self):
        return self.__annual_interest_rate_for_discount

    def set_annual_interest_rate_for_discount(self, annual_interest_rate_for_discount):
        self.__annual_interest_rate_for_discount = annual_interest_rate_for_discount

    def get_discount_times(self):
        return self.__discount_times

    def set_discount_times(self, discount_times):
        self.__discount_times = discount_times
