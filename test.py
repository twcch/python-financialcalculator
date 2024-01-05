from datetime import datetime
from dateutil.relativedelta import relativedelta

# 定義兩個日期
date1 = datetime(2022, 1, 15)
date2 = datetime(2022, 5, 20)

# 計算月份差
delta = relativedelta(date2, date1)

# 提取月份差
months_diff = delta.years * 12 + delta.months

print("Months Difference:", months_diff)
