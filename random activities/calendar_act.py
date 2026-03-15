import calendar

class InvalidValue(Exception):
    pass

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self , year , weekday):
        print(year , weekday)
        num_days = 0
        
        for month in range(1,13):
            for week in self.monthdays2calendar(year,month):
                if (0 , weekday) in week:
                    continue
                else:    
                    num_days += 1
        return num_days
            
try:
    year = int(input("Enter year: "))
    weekday = int(input("Enter weekday 0-6: "))
    if not -1 < weekday < 7:
        raise InvalidValue("Invalid input")
        
    mycal = MyCalendar()
    print(mycal.count_weekday_in_year(year , weekday))
    
except InvalidValue as e:
    print(e)
        