# Create a program that takes 2 strings as input. If the strings are the same length the program
# should print “The strings are the same length”. If they are not the same length the program
# shouldn’t print anything.

str1 = str(input("Enter a string: "))
str2 = str(input("Enter another string: "))

if len(str1) == len(str2):
    print("The strings are the same length")