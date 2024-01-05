from abc import ABC, abstractmethod


class SumAmountCalculatorService(ABC):
    @abstractmethod
    def calculate_monthly_interest_rate_for_discount(self):
        pass
