# find_min function definition goes here
def find_min(x, y):
    if x < y:
        minimum = x
    else:
        minimum = y    
    return minimum

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
minimum = find_min(first,second)
# Call the function here
print("Minimum: ", minimum)