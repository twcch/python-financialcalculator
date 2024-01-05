from datetime import datetime


class DateDifferenceCalculatorService:
    def __init__(self, str_start_date, str_end_date):
        self.__start_date = datetime.strptime(str_start_date, "%Y-%m-%d")
        self.__end_date = datetime.strptime(str_end_date, "%Y-%m-%d")

    def calculate_years_difference(self, adj_years):
        date_difference = self.__end_date - self.__start_date

        years = date_difference.days // 365 + adj_years

        return years

    def calculate_months_difference(self, adj_months):
        months = (
            (self.__end_date - self.__start_date) * 12
            + self.__end_date.month
            - self.__start_date.month
        )

        months = months + adj_months

        return months

    def calculate_days_difference(self, adj_days):
        date_difference = self.__end_date - self.__start_date

        days = date_difference.days + adj_days

        return days

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date
