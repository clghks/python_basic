import time

print(time.time())
print(time.ctime())
print(time.localtime())

now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_year, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))


import datetime

now = datetime.datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))


start = time.time()
for a in range(1000):
    print(a)
end = time .time()
print(end - start)

import calendar

print(calendar.calendar(2019))
print(calendar.month(2019, 10))

yoil = ["월", "화", "수", "목", "금", "토", "일"]
day = calendar.weekday(2019, 8, 15)
print("광복절은 " + yoil[day] + "요일이다.")