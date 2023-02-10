from datetime import datetime, timedelta

print(datetime(2000, 12, 12)-datetime.now())

fivehundread_days = timedelta(days = 500, hours = 12)
print(fivehundread_days + fivehundread_days+datetime.today())
