# Create a program that takes 2 integers as input, let’s call them low and high. Your program
# should print the sum of all the integers between low and high(low and high included) that are
# divisible by 3. You may assume that low is always lower than high.

low = int(input("Enter a integer: "))
high = int(input("Enter a integer: "))
sum1 = 0
for x in range(low, high + 1):
    if x % 3 == 0:
        sum1 += x
print(sum1)