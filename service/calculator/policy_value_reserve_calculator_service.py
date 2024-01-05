from abc import ABC, abstractmethod


class PolicyValueReserveCalculatorService(ABC):
    @abstractmethod
    def calculate_policy_value_reserve_on_base_sum_amount(self):
        pass

    @abstractmethod
    def calculate_policy_value_reserve_on_paid_up_sum_amount(self):
        pass

    @abstractmethod
    def calculate_policy_value_reserve_on_total_sum_amount(self):
        pass
