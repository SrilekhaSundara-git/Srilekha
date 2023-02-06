from datetime import datetime

print(datetime(1999,12,12))
print(datetime(1999,12,12,11,11,11))
print(datetime.today())
today = datetime.today()
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.weekday())
print(today.replace(year = 1992))
print(today.replace(year = 1992, month = 1, day = 21))