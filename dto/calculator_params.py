class CalculatorParams():
    
    def __init__(self):
        # 日期相關
        self.__coverage_start_date = None
        self.__coverage_end_date = None
        self.__coverage_period_days = 0
        
        # 計算日期相關
        self.__date_of_loss = None
        
        self.__period_start_date = None
        self.__period_end_date = None
        self.__period_days = 0
        
        self.__unrealized_premium_days = 0
        
        self.__insurance_year_at_date_of_loss = 0
        self.__policy_value_reserve_cumulative_days = 0
        
        # 倍數相關
        self.__sum_amount_multiple = 1
        self.__return_of_premium_multiple = 1
        self.__policy_value_reserve_multiple = 1
        
        # 結果比率相關
        self.__sum_amount_result_ratio = 1
        self.__return_of_premium_result_ratio = 1
        self.__policy_value_reserve_result_ratio = 1

