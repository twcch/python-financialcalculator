class ReturnOfPremiumCalculator:

    def __init__(self):
        self.__vpu = 10000
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0

    def calculate_return_of_premium_on_base_sum_amount(self):
        result = self.__calculate_sum_amount('B')

        return result

    def calculate_return_of_premium_on_paid_up_sum_amount(self):
        result = self.__calculate_sum_amount('P')

        return result

    def calculate_return_of_premium_on_total_sum_amount(self):
        result = self.__calculate_sum_amount('T')

        return result

    def __calculate_sum_amount(self, var):
        if (var == 'B'):
            unit_sum_amount = self.__unit_base_sum_amount
        
        if (var == 'P'):
            unit_sum_amount = self.__unit_paid_up_sum_amount
        
        if (var == 'T'):
            unit_sum_amount = self.__unit_base_sum_amount + self.__unit_paid_up_sum_amount
        
        result = round(decimal.Decimal(unit_sum_amount * vpu))

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