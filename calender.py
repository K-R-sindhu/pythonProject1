import calendar

date = list(map(int,input().split(' ')))
week = ['MONDAY',"TUESDAY",'WEDNESDAY',"THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(week[calendar.weekday(date[2], date[0], date[1])])