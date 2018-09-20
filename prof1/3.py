# To determine whether a year is a leap year, follow these steps: 
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).

year = int(input("Enter a year: "))

leap_year = "This year is a leap year"
not_leap_year = "This year is not a leap year"

if year % 2 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(leap_year)
        else:
            print(not_leap_year)
    else:
        print(leap_year)
else:
    print(not_leap_year)