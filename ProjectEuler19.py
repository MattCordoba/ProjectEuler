__author__ = 'matt cordoba'
import datetime
def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 != 0:
            return False
    if year % 4 ==0: return True
    return False

tempDate = datetime.date(1900,1,1)
dateTracker = 2 # 2 = TUESDAY
count = 0
for y in range (1901,2001):
    for x in range (1,13):
        tempDate = datetime.date(y,x,1)
        tempVal = 0
        if dateTracker == 0: # 0 = SUNDAY
            count = count + 1
        if tempDate.month == 1 or tempDate.month == 3 or tempDate.month == 5 or tempDate.month == 7 or tempDate.month == 8 or tempDate.month == 10 or tempDate.month == 12:
            tempVal = dateTracker + 3 -7
            if(tempVal < 0):
                dateTracker += 3
            else:
                dateTracker += -4
        elif tempDate.month == 2:
            if(not isLeapYear(tempDate.year)):
                tempVal = dateTracker + 0 -7
                if(tempVal >= 0):
                    dateTracker += -7
            else:
                tempVal = dateTracker + 1 -7
                if(tempVal < 0):
                    dateTracker += 1
                else:
                    dateTracker += -6
        else:
            tempVal = dateTracker + 2 -7
            if(tempVal < 0):
                dateTracker += 2
            else:
                dateTracker += -5

print count