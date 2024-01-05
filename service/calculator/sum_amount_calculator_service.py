from abc import ABC, abstractmethod


class SumAmountCalculatorService(ABC):
    @abstractmethod
    def calculate_sum_amount_on_base_sum_amount(self):
        pass

    @abstractmethod
    def calculate_sum_amount_on_paid_up_sum_amount(self):
        pass

    @abstractmethod
    def calculate_sum_amount_on_total_sum_amount(self):
        pass
