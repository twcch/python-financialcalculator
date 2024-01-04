import decimal
from dto.benefit_params import BenefitParams

class DiscountCalculatorService():
    
    def __init__(self, benefit_params):
        self.__benefit_params = benefit_params
    
    def calculate_monthly_discount_rate(self):
        annual_discount_rate = self.__benefit_params.get_annual_discount_rate()
        monthly_discount_rate = round(decimal.Decimal((1 + annual_discount_rate) ** (1 / 12) - 1), 9)
        return monthly_discount_rate
    
    def calculate_discount_amount(self):
        pass