class PolicyValueReserveCalculator:

    def __init__(self):
        self.__beginning_policy_value_reserve = 0
        self.__ending_policy_value_reserve = 0
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__multiple = 1
        self.__result_ratio = 1



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
