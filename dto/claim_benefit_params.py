from datetime import datetime


class ClaimBenefitParams:
    def __init__(self):
        # 險種相關變數
        self.__coverage_start_date = datetime(1911, 1, 1)
        self.__currency = "NTD"
        self.__payment_frequency = "A"
        self.__payment_period = 0
        self.__vpu = 10000

        # 理賠相關變數
        self.__date_of_loss = datetime(1911, 1, 1)
        self.__insurance_year_at_date_of_loss = (
            self.__calculate_insurance_year_at_date_of_loss()
        )

        # 保險費相關變數
        self.__annualized_standard_unit_premium = 0
        self.__multiple_for_return_of_premium = 1
        self.__result_ratio_for_return_of_premium = 1

        # 保單價值準備金相關變數
        self.__beginning_policy_value_reserve = 0
        self.__ending_policy_value_reserve = 0
        self.__cumulative_days_for_policy_value_reserve = (
            self.__calculate_cumulative_days_for_policy_value_reserve()
        )
        self.__period_days_for_policy_value_reserve = (
            self.__calculate_period_days_for_policy_value_reserve()
        )
        self.__multiple_for_policy_value_reserve = 1
        self.__result_ratio_for_policy_value_reserve = 1

        # 保險金額相關變數
        self.__unit_base_sum_amount = 0
        self.__unit_paid_up_sum_amount = 0
        self.__multiple_for_sum_amount = 1
        self.__result_ratio_for_sum_amount = 1

        # 貼現相關變數
        self.__payment_amount = 0
        self.__annual_interest_rate_for_discount = 0
        self.__discount_times = 0

    def __calculate_insurance_year_at_date_of_loss(self):
        pass

    def __calculate_cumulative_days_for_policy_value_reserve(self):
        pass

    def __calculate_period_days_for_policy_value_reserve(self):
        pass

    def get_coverage_start_date(self):
        return self.__coverage_start_date

    def set_coverage_start_date(self, coverage_start_date):
        self.__coverage_start_date = coverage_start_date

    def get_currency(self):
        return self.__currency

    def set_currency(self, currency):
        self.__currency = currency

    def get_payment_frequency(self):
        return self.__payment_frequency

    def set_payment_frequency(self, payment_frequency):
        self.__payment_frequency = payment_frequency

    def get_payment_period(self):
        return self.__payment_period

    def set_payment_period(self, payment_period):
        self.__payment_period = payment_period

    def get_vpu(self):
        return self.__vpu

    def set_vpu(self, vpu):
        self.__vpu = vpu

    def get_date_of_loss(self):
        return self.__date_of_loss

    def set_date_of_loss(self, date_of_loss):
        self.__date_of_loss = date_of_loss

    def get_insurance_year_at_date_of_loss(self):
        return self.__insurance_year_at_date_of_loss

    def get_annualized_standard_unit_premium(self):
        return self.__annualized_standard_unit_premium

    def set_annualized_standard_unit_premium(self, annualized_standard_unit_premium):
        self.__annualized_standard_unit_premium = annualized_standard_unit_premium

    def get_multiple_for_return_of_premium(self):
        return self.__multiple_for_return_of_premium

    def set_multiple_for_return_of_premium(self, multiple_for_return_of_premium):
        self.__multiple_for_return_of_premium = multiple_for_return_of_premium

    def get_result_ratio_for_return_of_premium(self):
        return self.__result_ratio_for_return_of_premium

    def set_result_ratio_for_return_of_premium(
        self, result_ratio_for_return_of_premium
    ):
        self.__result_ratio_for_return_of_premium = result_ratio_for_return_of_premium

    def get_beginning_policy_value_reserve(self):
        return self.__beginning_policy_value_reserve

    def set_beginning_policy_value_reserve(self, beginning_policy_value_reserve):
        self.__beginning_policy_value_reserve = beginning_policy_value_reserve

    def get_ending_policy_value_reserve(self):
        return self.__ending_policy_value_reserve

    def set_ending_policy_value_reserve(self, ending_policy_value_reserve):
        self.__ending_policy_value_reserve = ending_policy_value_reserve

    def get_cumulative_days_for_policy_value_reserve(self):
        return self.__cumulative_days_for_policy_value_reserve

    def get_period_days_for_policy_value_reserve(self):
        return self.__period_days_for_policy_value_reserve

    def get_multiple_for_policy_value_reserve(self):
        return self.__multiple_for_policy_value_reserve

    def set_multiple_for_policy_value_reserve(self, multiple_for_policy_value_reserve):
        self.__multiple_for_policy_value_reserve = multiple_for_policy_value_reserve

    def get_result_ratio_for_policy_value_reserve(self):
        return self.__result_ratio_for_policy_value_reserve

    def set_result_ratio_for_policy_value_reserve(
        self, result_ratio_for_policy_value_reserve
    ):
        self.__result_ratio_for_policy_value_reserve = (
            result_ratio_for_policy_value_reserve
        )

    def get_unit_base_sum_amount(self):
        return self.__unit_base_sum_amount

    def set_unit_base_sum_amount(self, unit_base_sum_amount):
        self.__unit_base_sum_amount = unit_base_sum_amount

    def get_unit_paid_up_sum_amount(self):
        return self.__unit_paid_up_sum_amount

    def set_unit_paid_up_sum_amount(self, unit_paid_up_sum_amount):
        self.__unit_paid_up_sum_amount = unit_paid_up_sum_amount

    def get_multiple_for_sum_amount(self):
        return self.__multiple_for_sum_amount

    def set_multiple_for_sum_amount(self, multiple_for_sum_amount):
        self.__multiple_for_sum_amount = multiple_for_sum_amount

    def get_result_ratio_for_sum_amount(self):
        return self.__result_ratio_for_sum_amount

    def set_result_ratio_for_sum_amount(self, result_ratio_for_sum_amount):
        self.__result_ratio_for_sum_amount = result_ratio_for_sum_amount

    def get_payment_amount(self):
        return self.__payment_amount

    def set_payment_amount(self, payment_amount):
        self.__payment_amount = payment_amount

    def get_annual_interest_rate_for_discount(self):
        return self.__annual_interest_rate_for_discount

    def set_annual_interest_rate_for_discount(self, annual_interest_rate_for_discount):
        self.__annual_interest_rate_for_discount = annual_interest_rate_for_discount

    def get_discount_times(self):
        return self.__discount_times

    def set_discount_times(self, discount_times):
        self.__discount_times = discount_times
