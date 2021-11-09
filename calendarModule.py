def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def lastDay(year, month):
    m=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if isLeapYear(year):
        m[1]=29
    else:
        m[1]=28

    return m[month -1]

def totalDay(year, month, day):
    total=(year-1)*365+(year-1)//4-(year-1)//100+(year-1)//400

    for i in range(1, month):
        total+=lastDay(year, i)

    return total + day

def weekDay(year, month, day):
    return totalDay(year, month ,day) % 7

