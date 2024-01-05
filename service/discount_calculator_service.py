from abc import ABC, abstractmethod

class DiscountCalculatorService(ABC):

    @abstractmethod
    def calculate_monthly_interest_rate_for_discount(self):
        pass

    @abstractmethod
    def calculate_monthly_discount_rate(self):
        pass

    @abstractmethod
    def calculate_discount_amount(self):
        pass
