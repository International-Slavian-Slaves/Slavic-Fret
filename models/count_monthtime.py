from datetime import datetime

datetime_str = "2012-03-12 14:20:10"
datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print(datetime_obj.year)
print(datetime.now().__str__())