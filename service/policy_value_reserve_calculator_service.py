import decimal

class PolicyValueReserveCalculatorService:

    def __init__(self):
        self.__beginning_policy_value_reserve = 0
        self.__ending_policy_value_reserve = 0
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__cumulative_days = 0
        self.__period_days = 0
        self.__multiple = 1
        self.__result_ratio = 1

    def calculate_policy_value_reserve_on_base_sum_amount(self):
        result = self.__calculate_policy_value_reserve('B')

        return result

    def calculate_policy_value_reserve_on_paid_up_sum_amount(self):
        result = self.__calculate_policy_value_reserve('P')

        return result

    def calculate_policy_value_reserve_on_total_sum_amount(self):
        result = self.__calculate_policy_value_reserve('T')

        return result

    def __calculate_policy_value_reserve(self, var):
        if (var == 'B'):
            unit_sum_amount = self.__unit_base_sum_amount
        
        if (var == 'P'):
            unit_sum_amount = self.__unit_paid_up_sum_amount
        
        if (var == 'T'):
            unit_sum_amount = self.__unit_base_sum_amount + self.__unit_paid_up_sum_amount
        
        result = round(decimal.Decimal(((self.__ending_policy_value_reserve - self.__beginning_policy_value_reserve) * self.__cumulative_days / self.__period_days + self.__beginning_policy_value_reserve) * unit_sum_amount))

        return result

    def get_beginning_policy_value_reserve(self):
        return self.__beginning_policy_value_reserve
    
    def set_beginning_policy_value_reserve(self, beginning_policy_value_reserve):
        self.__beginning_policy_value_reserve = beginning_policy_value_reserve

    def get_ending_policy_value_reserve(self):
        return self.__ending_policy_value_reserve
    
    def set_ending_policy_value_reserve(self, ending_policy_value_reserve):
        self.__ending_policy_value_reserve = ending_policy_value_reserve

    def get_unit_base_sum_amount(self):
        return self.__unit_base_sum_amount
    
    def set_unit_base_sum_amount(self, unit_base_sum_amount):
        self.__unit_base_sum_amount = unit_base_sum_amount
    
    def get_unit_paid_up_sum_amount(self):
        return self.__unit_paid_up_sum_amount
    
    def set_uunit_paid_up_sum_amount(self, unit_paid_up_sum_amount):
        self.__unit_paid_up_sum_amount = unit_paid_up_sum_amount

    def get_cumulative_days(self):
        return self.__cumulative_days
    
    def set_cumulative_days(self, cumulative_days):
        self.__cumulative_days = cumulative_days

    def get_period_days(self):
        return self.__period_days
    
    def set_period_days(self, period_days):
        self.__period_days = period_days

    def get_multiple(self):
        return self.__multiple
    
    def set_multiple(self, multiple):
        self.__multiple = multiple

    def get_result_ratio(self):
        return self.__result_ratio
    
    def set_result_ratio(self, result_ratio):
        self.__result_ratio = result_ratio
