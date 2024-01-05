from abc import ABC, abstractmethod


class DateCalculatorService(ABC):
    @abstractmethod
    def calculate_years_difference(self):
        pass

    @abstractmethod
    def calculate_months_difference(self):
        pass

    @abstractmethod
    def calculate_days_difference(self):
        pass

    @abstractmethod
    def adjust_years_to_date(self):
        pass

    @abstractmethod
    def adjust_months_to_date(self):
        pass

    @abstractmethod
    def adjust_days_to_date(self):
        pass
