# Create a program that takes 2 integers as input, let’s call them low and high. Your program
# should output all the integers between low and high but only if the value of low is lower than the
# value of high. (if printed the values of low and high should be included).

low = int(input("Enter a integer: "))
high = int(input("Enter second integer: "))

for x in range(low - 1, high):
    x += 1
    if low < high:
        print(x)