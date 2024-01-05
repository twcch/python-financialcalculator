from abc import ABC, abstractmethod


class DateCalculatorService(ABC):
    @abstractmethod
    def calculate_days_difference(self):
        pass