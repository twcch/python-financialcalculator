class CoverageParams():
    
    def __init__(self):
        # 基本資料相關
        self.__coverage = None
        self.__currency = 'NTD'
        self.__payment_period = 0
        
        # 保險金額相關
        self.__vpu = 10000
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        
        # 保險費相關
        self.__annualized_standard_unit_premium = 0
        
        # 保單價值準備金相關
        self.__beginning_policy_value_reserve = 0
        self.__ending_policy_value_reserve = 0
    
    def get_coverage(self):
        return self.__coverage
    
    def set_coverage(self, coverage):
        self.__coverage = coverage
    
    def get_currency(self):
        return self.__currency
    
    def set_currency(self, currency):
        self.__currency = currency

    def get_payment_period(self):
        return self.__payment_period
    
    def set_payment_period(self, payment_period):
        self.__payment_period = payment_period

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

    def get_annualized_standard_unit_premium(self):
        return self.__annualized_standard_unit_premium
    
    def set_annualized_standard_unit_premium(self, annualized_standard_unit_premium):
        self.__annualized_standard_unit_premium = annualized_standard_unit_premium
    
    def get_beginning_policy_value_reserve(self):
        return self.__beginning_policy_value_reserve
    
    def set_beginning_policy_value_reserve(self, beginning_policy_value_reserve):
        self.__beginning_policy_value_reserve = beginning_policy_value_reserve
    
    def get_ending_policy_value_reserve(self):
        return self.__ending_policy_value_reserve
    
    def set_ending_policy_value_reserve(self, ending_policy_value_reserve):
        self.__ending_policy_value_reserve = ending_policy_value_reserve