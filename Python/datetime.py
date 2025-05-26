import datetime
mytime = datetime.time(2, 1, 1, 1) 
# ✅ Correct (hour, minute, second, microsecond)
print(mytime) 
# Output: 02:01:01.000001

today=datetime.date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)


print(today.ctime())

from datetime import date
print(date.today)
cYear=date(2025,1,1)
lYear=date(2024,1,1)
print((cYear-lYear).days) #diff in number of days 
#or 

_diff=cYear-lYear
print(type(_diff))

days=_diff.days
seconds=_diff.seconds

print(days)
print(seconds)


