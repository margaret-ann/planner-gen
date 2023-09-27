# Playing with Calendar library

import calendar as cal

year = 2023
month = 9

obj = cal.Calendar()

for day in obj.itermonthdays(year, month):
    print(day)
