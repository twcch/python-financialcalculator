from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    # 將輸入日期轉換為 datetime 對象
    input_datetime = datetime.strptime(input_date, "%Y-%m-%d")

    # 使用 timedelta 增加天數
    result_datetime = input_datetime + timedelta(days=days_to_add)

    return result_datetime

# 測試方法
input_date = "2022-01-15"
days_to_add = 30

result = add_days_to_date(input_date, days_to_add)
print("Result:", type(result))
