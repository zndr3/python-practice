# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44

from datetime import datetime , date

from matplotlib import widgets

# print(datetime.now())
dt = datetime(2020 , 11 , 4, 14 , 53 , 00)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %u"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %U"))
