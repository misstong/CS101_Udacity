def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    sum=0
    while not(year1==year2 and month1==month2 and day1==day2):
        sum+=1
        year1,month1,day1=next_day(year1,month1,day1)
    return sum

def next_day(year1,month1,day1):
    if day1<dayofmonth(year1,month1):
        return year1,month1,day1+1
    if month1<12:
        return year1,month1+1,1
    return year1+1,1,1

def dayofmonth(year1,month1):
    month_days=[31,31,28,31,
                30,31,30,
                31,31,30,
                31,30,31]
    if leap_year(year1)==1 and month1==2:
        return 29
    return month_days[month1]

def leap_year(year1):
    if year1%4!=0:
        return 0
    elif year1%100!=0:
        return 1
    elif year1%400!=0:
        return 0
    else:
        return 1
print daysBetweenDates(2012,1,1,2012,2,28)
print daysBetweenDates(2012,1,1,2012,3,1)
print daysBetweenDates(2011,6,30,2012,6,30)
print daysBetweenDates(2011,1,1,2012,8,8)
print daysBetweenDates(1900,1,1,1999,12,31)
