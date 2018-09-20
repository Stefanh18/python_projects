month = str(input("Month: "))
day = int(input("Day: "))


if month == 'december' and day == 25:
    print("Christmas day")
elif month == 'june' and day == 17:
    print("National holiday")
elif month == 'january' and day == 1:
    print("New year's day")
else:
    print("Not a holiday")