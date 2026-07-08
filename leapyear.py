def leap_year(year):
    if year % 400 == 0 :
        return " Leap Year"
    elif year % 100 == 0:
        return " Not a leap year"
    elif year % 4 == 0 :
        return " Leap year"
    else:
        return " Not a leap year"
result = leap_year(1900)
print(result)