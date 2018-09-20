# is_prime function definition goes here
def is_prime(x):
    counter = 2
    prime = True
    while counter < x:
        if x % counter ==0:
            prime = False
        counter += 1 
    return prime

num = int(input("Input an integer greater than 1: "))
true_or_false = is_prime(num)
# Call the function here and print out the appropriate message

if true_or_false == True:
    print(num, "is a prime")
else:
    print(num, "is not a prime" )

