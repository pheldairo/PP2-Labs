from datetime import datetime

date_str1 = "2025-02-01 12:00:00"
date_str2 = "2025-01-02 15:30:45"


date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")


print(abs((date1 - date2)).total_seconds())