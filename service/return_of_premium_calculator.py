class ReturnOfPremiumCalculator:

    def __init__(self):
        self.__annualized_standard_unit_premium = 0
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__payment_period = 0
        self.__insurance_year_at_date_of_loss = 0
        self.__spillover_multiple = 1
        self.__benefit_ratio = 1
    
    def get_annualized_standard_unit_premium(self):
        return self.__annualized_standard_unit_premium

    def set_annualized_standard_unit_premium(self, annualized_standard_unit_premium):
        self.__annualized_standard_unit_premium = annualized_standard_unit_premium
    
    def get_unit_base_sum_amount(self):
        return self.__unit_base_sum_amount
    
    def set_unit_base_sum_amount(self, unit_base_sum_amount):
        self.__unit_base_sum_amount = unit_base_sum_amount
    
    def get_unit_paid_up_sum_amount(self):
        return self.__unit_paid_up_sum_amount
    
    def set_uunit_paid_up_sum_amount(self, unit_paid_up_sum_amount):
        self.__unit_paid_up_sum_amount = unit_paid_up_sum_amount

    def get_payment_period(self):
        return self.__payment_period
    
    def set_payment_period(self, payment_period):
        self.__payment_period = payment_period

    def get_insurance_year_at_date_of_loss(self):
        return self.__insurance_year_at_date_of_loss
    
    def set_insurance_year_at_date_of_loss(self, insurance_year_at_date_of_loss):
        self.__insurance_year_at_date_of_loss = insurance_year_at_date_of_loss

    def get_spillover_multiple(self):
        return self.__spillover_multiple
    
    def set_spillover_multiple(self, spillover_multiple):
        self.__spillover_multiple = spillover_multiple

    def get_benefit_ratio(self):
        return self.__benefit_ratio
    
    def set_benefit_ratio(self, benefit_ratio):
        self.__benefit_ratio = benefit_ratio
