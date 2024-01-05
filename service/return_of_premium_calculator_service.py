from abc import ABC, abstractmethod


class ReturnOfPremiumCalculatorService(ABC):
    @abstractmethod
    def calculate_return_of_premium_on_base_sum_amount(self):
        pass

    @abstractmethod
    def calculate_return_of_premium_on_paid_up_sum_amount(self):
        pass

    @abstractmethod
    def calculate_return_of_premium_on_total_sum_amount(self):
        pass
