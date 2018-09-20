# The function definition goes here
def integer(x):
    if 1 < x < 555:
        x = str(x) + " is in range."
    else:
        x = str(x) + " is outside the range!"
    return x


num = int(input("Enter a number: "))
print(integer(num))
# You call the function here