# Create a program that takes 1 integer as input. The program should print ”Less than 10” if the
# input value is less than 10. If the input value is greater than or equal to 10 and less than 20 it
# should print “between 10 and 20”. If the input value is greater than or equal to 20 the program
# should print “the value is too high!” and if the input value is less than 0 the program should print
# “too low”.

my_int = int(input("Enter a integer: "))

if my_int < 10 and my_int >= 0:
    print("Less than 10")
elif my_int >= 10 and my_int < 20:
    print("between 10 and 20")
elif my_int >= 20:
    print("the value is too high!")
else:
    print("too low")