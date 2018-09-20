# Create a program that takes 2 integers as input, let’s call them low and high. Your program
# should print all the integers between low and high (low and high included). You may assume that
# low is always lower than high.
low = int(input("Enter a integer: "))
high = int(input("Enter second integer: "))
x = 0
for x in range(low + 1, high):
    print(x)
    x += 1
