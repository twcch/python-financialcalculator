class ClaimBenefitParams():

    def __init__(self):
        # 貼現
        self.__payment_amount = 0
        self.__annual_interest_rate_for_discount = 0
        self.__discount_times = 0

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
