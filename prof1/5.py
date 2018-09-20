# Write a Python program using a for loop that, given a integer n, prints out all the Armstrong number between 0 and n.  
# You can assume that the maximum is 999.
# An Armstrong number is a number that is equal to the sum of its digits when each digit is raised to the number of digits.
# For example:
# 6 is an Armstrong number because 6**1 = 6
# 153 is an Armstrong number because 1**3 + 5**3 + 3**3 = 153
n = int(input("Enter a number between 0 and 999: "))

for x in range(0, n + 1):
    if x < 10:
        num_digit = 1
        third = 0
        second = 0
        first = x
    elif x < 100:
        num_digit = 2
        third = 0
        second = x // 10
        first = x % 10
    else:
        num_digit = 3
        third = x // 100
        second = (x % 100) // 10
        first = (x % 100) % 10
    if (third ** num_digit + second ** num_digit + first ** num_digit == x):
        print(x)
