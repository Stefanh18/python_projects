# 5. Create a program that takes 2 strings as input, let´s call them firstname and lastname. They
# should hold (as the names of them imply) the first and last name of the user. Next you should
# create a variable called fullname which stores the concatenated value of the variables firstname
# and lastname. Finally, the program should print the text “Your full name is <fullname>” where
# <fullname> is the value of the variable fullname.
firstname = str(input("Enter your first name: "))
lastname = str(input("Enter your last name: "))
bil = (" ")
fullname = firstname + bil + lastname

print("Your full nam is", fullname)