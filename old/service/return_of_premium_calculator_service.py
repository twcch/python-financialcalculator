import decimal
import math


class ReturnOfPremiumCalculatorService:
    def __init__(self):
        self.__currency = "NTD"
        self.__annualized_standard_unit_premium = 0
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__payment_period = 0
        self.__insurance_year_at_date_of_loss = 0
        self.__spillover_multiple = 1
        self.__result_ratio = 1

    def calculate_return_of_premium_on_base_sum_amount(self):
        result = self.__calculate_return_of_premium("B")

        return result

    def calculate_return_of_premium_on_paid_up_sum_amount(self):
        result = self.__calculate_return_of_premium("P")

        return result

    def calculate_return_of_premium_on_total_sum_amount(self):
        result = self.__calculate_return_of_premium("T")

        return result

    def __calculate_return_of_premium(self, var):
        unit_premium = round(
            decimal.Decimal(
                self.__annualized_standard_unit_premium
                * self.__spillover_multiple
                * min(self.__payment_period, self.__insurance_year_at_date_of_loss)
            ),
            1,
        )

        if var == "B":
            unit_sum_amount = self.__unit_base_sum_amount

        if var == "P":
            unit_sum_amount = self.__unit_paid_up_sum_amount

        if var == "T":
            unit_sum_amount = (
                self.__unit_base_sum_amount + self.__unit_paid_up_sum_amount
            )

        if self.__currency == "NTD":
            result = round(decimal.Decimal(unit_premium * unit_sum_amount))

        if self.__currency == "USD":
            result = math.ceil(decimal.Decimal(unit_premium * unit_sum_amount))

        result = round(decimal.Decimal(result * self.__result_ratio))

        return result

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_annualized_standard_unit_premium(self):
        return self.__annualized_standard_unit_premium

    def set_annualized_standard_unit_premium(self, annualized_standard_unit_premium):
        self.__annualized_standard_unit_premium = annualized_standard_unit_premium

    def get_unit_base_sum_amount(self):
        return self.__unit_base_sum_amount

    def set_unit_base_sum_amount(self, unit_base_sum_amount):
        self.__unit_base_sum_amount = unit_base_sum_amount

    def get_unit_paid_up_sum_amount(self):
        return self.__unit_paid_up_sum_amount

    def set_uunit_paid_up_sum_amount(self, unit_paid_up_sum_amount):
        self.__unit_paid_up_sum_amount = unit_paid_up_sum_amount

    def get_payment_period(self):
        return self.__payment_period

    def set_payment_period(self, payment_period):
        self.__payment_period = payment_period

    def get_insurance_year_at_date_of_loss(self):
        return self.__insurance_year_at_date_of_loss

    def set_insurance_year_at_date_of_loss(self, insurance_year_at_date_of_loss):
        self.__insurance_year_at_date_of_loss = insurance_year_at_date_of_loss

    def get_spillover_multiple(self):
        return self.__spillover_multiple

    def set_spillover_multiple(self, spillover_multiple):
        self.__spillover_multiple = spillover_multiple

    def get_result_ratio(self):
        return self.__result_ratio

    def set_result_ratio(self, result_ratio):
        self.__result_ratio = result_ratio
