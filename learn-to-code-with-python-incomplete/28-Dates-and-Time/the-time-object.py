from datetime import time
import datetime
now = datetime.datetime.now()
print(now)
start = time()
print(start)
print(now.time())
print(time(12,12,12))
hours = time(10,10,10)
print(hours.hour)
print(hours.minute)
print(hours.second)