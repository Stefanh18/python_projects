m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line
highest = 0
if m < n:
    high = n - 1
else:
    high = m - 1
for x in range(2,high):
    if m % x == 0 and n % x == 0:
        highest = x
        
print(highest)
