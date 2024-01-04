class BenefitParams():
    
    def __init__(self):
        # 貼現
        self.__payment_amount = 0
        self.__annual_discount_rate = 0
        self.__discount_times = 0

    def get_payment_amount(self):
        return self.__payment_amount

    def set_payment_amount(self, value):
        self.__payment_amount = value

    def get_annual_discount_rate(self):
        return self.__annual_discount_rate

    def set_annual_discount_rate(self, value):
        self.__annual_discount_rate = value

    def get_discount_times(self):
        return self.__discount_times

    def set_discount_times(self, value):
        self.__discount_times = value